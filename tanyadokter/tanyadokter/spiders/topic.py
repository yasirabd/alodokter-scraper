import html
import json
import scrapy
from tanyadokter.items import TopicItem


class TopicSpider(scrapy.Spider):
    name = "topic"
    allowed_domains = ["alodokter.com"]
    start_urls = ["https://www.alodokter.com/komunitas/topik#"]

    def parse(self, response):
        raw_json = response.xpath('//search-a-z-topic/@search-results').get()
        if raw_json:
            decoded_json = html.unescape(raw_json)
            try:
                topics = json.loads(decoded_json)
                for topic in topics:
                    item = TopicItem()
                    item['topic'] = topic.get('post_title')
                    item['url'] = response.urljoin(f"/komunitas/topic-tag/{topic.get('permalink')}")
                    yield item
            except json.JSONDecodeError:
                self.logger.error("Gagal memuat JSON.")
        else:
            self.logger.error("Atribut 'search-results' tidak ditemukan.")