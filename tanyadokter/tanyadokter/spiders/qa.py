import csv
from datetime import datetime
import html
import re
import scrapy
from tanyadokter.items import QuestionAnswerItem


class QASpider(scrapy.Spider):
    name = "qa"
    allowed_domains = ["alodokter.com"]

    def start_requests(self):
        with open('dev-topic.csv', newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                topic = row['topic']
                url = row['url']
                yield scrapy.Request(url=url, meta={'topic': topic}, callback=self.parse)

    def parse(self, response):
        topic = response.meta['topic']
        hrefs = response.xpath('//card-topic/@href').getall()
        for href in hrefs:
            url = response.urljoin(href)
            yield scrapy.Request(url=url, meta={'topic': topic}, callback=self.parse_question_answer)

        # next page
        next_page = response.xpath('//paginate-button/@next-page').get()
        if next_page != "0":
            base_url = response.xpath('//paginate-button/@base-url').get()
            next_page = response.urljoin(f"{base_url}page/{next_page}")
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_question_answer(self, response):
        # Extract the question and answer from the response
        item = QuestionAnswerItem()
        item['topic_category'] = response.meta['topic']
        item['question_title'] = response.xpath('//detail-topic/@member-topic-title').get()
        item['question_body'] = self.clean_text(response.xpath('//detail-topic/@member-topic-content').get())
        item['question_date'] = self.parse_date(response.xpath('//detail-topic/@member-post-date').get())
        item['doctor_name'] = response.xpath('//doctor-topic/@by-doctor').get()
        item['answer_body'] = self.clean_text(response.xpath('//doctor-topic/@doctor-topic-content').get())
        item['answer_date'] = self.parse_date(response.xpath('//doctor-topic/@post-date').get())
        yield item

    def parse_date(self, date_string):
        # Map Indonesian month names
        bulan = {
            'Januari': 'January', 'Februari': 'February', 'Maret': 'March', 'April': 'April',
            'Mei': 'May', 'Juni': 'June', 'Juli': 'July', 'Agustus': 'August',
            'September': 'September', 'Oktober': 'October', 'November': 'November', 'Desember': 'December'
        }

        # Replace month name with number
        for indo_month, number in bulan.items():
            if indo_month in date_string:
                date_string = date_string.replace(indo_month, number)
                break
        
        # Parse to datetime object
        parsed_date = datetime.strptime(date_string, '%d %B %Y, %H:%M')
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')
    
    def clean_text(self, text):
        decoded_text = text.encode('utf-8').decode('unicode_escape')

        # Remove anchor tags but keep the text inside
        cleaned_text = re.sub(r'<a [^>]+>(.*?)</a>', r'\1', decoded_text)

        # Remove all other HTML tags
        cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)

        # Remove extra newline
        cleaned_text = re.sub(r'\n+', '\n', cleaned_text)

        # Final strip/cleanup
        cleaned_text = cleaned_text.strip()

        return cleaned_text