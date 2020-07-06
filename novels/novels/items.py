# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    novel_name = scrapy.Field()
    novel_author = scrapy.Field()
    novel_classification = scrapy.Field()
    novel_status = scrapy.Field()
    # novel_number_of_words = scrapy.Field()
    novel_brief_introduction = scrapy.Field()
