# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import pymysql
from itemadapter import ItemAdapter


class NovelsPipeline:
    def __init__(self):
        self.fp = open('qidian.csv', 'w', encoding='utf8')
        self.fp.write("小说名")
        self.fp.write("\t")
        self.fp.write("作者名")
        self.fp.write("\t")
        self.fp.write("分类")
        self.fp.write("\t")
        self.fp.write("状态")
        self.fp.write("\t")
        self.fp.write("简介")
        self.fp.write("\n")

    def process_item(self, item, spider):
        for i in range(20):
            novel_name = item['novel_name'][i]
            novel_author = item['novel_author'][i]
            novel_classification = item['novel_classification'][i]
            novel_status = item['novel_status'][i]
            novel_brief_introduction = item['novel_brief_introduction'][i]
            # item_list = []
            # item_list.append(novel_name)
            # item_list.append(novel_author)
            # item_list.append(novel_classification)
            # item_list.append(novel_status)
            # item_list.append(novel_brief_introduction)
            # print(item_list)
            self.fp.write(item['novel_name'][i])
            self.fp.write('\t')
            self.fp.write(item['novel_author'][i])
            self.fp.write('\t')
            self.fp.write(item['novel_classification'][i])
            self.fp.write('\t')
            self.fp.write(item['novel_status'][i])
            self.fp.write('\t')
            self.fp.write(item['novel_brief_introduction'][i])
            self.fp.write('\n')

            print("小说名: " + novel_name)
            print("小说作者: " + novel_author)
            print("小说性质: " + novel_classification)
            print("小说状态: " + novel_status)
            print("小说简介: " + novel_brief_introduction)

        return item

    def close_spider(self, spider):
        self.fp.close()


from scrapy.utils.project import get_project_settings


class NovelsMYSQLPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings["HOST"]
        port = settings["PORT"]
        user = settings["USER"]
        password = settings["PASSWORD"]
        db = settings["DBNAME"]
        # charset = settings["CHARSET"]

        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)

    def process_item(self, item, spider):
        for i in range(20):
            novel_name = item['novel_name'][i]
            novel_author = item['novel_author'][i]
            novel_classification = item['novel_classification'][i]
            novel_status = item['novel_status'][i]
            novel_brief_introduction = item['novel_brief_introduction'][i]
            # item_list = []
            # item_list.append(novel_name)
            # item_list.append(novel_author)
            # item_list.append(novel_classification)
            # item_list.append(novel_status)
            # item_list.append(novel_brief_introduction)
            # print(item_list)

            print("小说名: " + novel_name)
            print("小说作者: " + novel_author)
            print("小说性质: " + novel_classification)
            print("小说状态: " + novel_status)
            print("小说简介: " + novel_brief_introduction)

            sql = 'insert into qidian(novel_name,novel_author,novel_classification,novel_status,novel_brief_introduction) values ("%s","%s","%s","%s","%s")' % \
                  (novel_name, novel_author, novel_classification, novel_status, novel_brief_introduction)
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()
