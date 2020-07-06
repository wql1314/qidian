# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class NovelsPipeline:
    def __init__(self):
        self.fp = open('qidian.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        for i in range(20):
            novel_name = item['novel_name'][i]
            novel_author = item['novel_author'][i]
            novel_classification = item['novel_classification'][i]
            novel_status = item['novel_status'][i]
            novel_brief_introduction = item['novel_brief_introduction'][i]
            print("小说名: " + novel_name)
            print("小说作者: " + novel_author)
            print("小说性质: " + novel_classification)
            print("小说状态: " + novel_status)
            print("小说简介: " + novel_brief_introduction)

        return item

    def close_spider(self, spider):
        self.fp.close()
