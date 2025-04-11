import csv
import scrapy


class QASpider(scrapy.Spider):
    name = "qa"
    allowed_domains = ["alodokter.com"]

    def start_requests(self):
        with open('dev-topic.csv', newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                url = row['url']
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        hrefs = response.xpath('//card-topic/@href').getall()
        for href in hrefs:
            url = response.urljoin(href)
            # yield scrapy.Request(url=url, callback=self.parse_question)

        # next page
        next_page = response.xpath('//paginate-button/@next-page').get()
        if next_page != "0":
            base_url = response.xpath('//paginate-button/@base-url').get()
            next_page = response.urljoin(f"{base_url}page/{next_page}")
            yield scrapy.Request(url=next_page, callback=self.parse)