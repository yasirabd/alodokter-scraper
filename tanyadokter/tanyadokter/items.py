# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    topic = scrapy.Field()
    url = scrapy.Field()


class QuestionAnswerItem(scrapy.Item):
    topic_category = scrapy.Field()
    question_title = scrapy.Field()
    question_body = scrapy.Field()
    question_date = scrapy.Field()
    doctor_name = scrapy.Field()
    answer_body = scrapy.Field()
    answer_date = scrapy.Field()