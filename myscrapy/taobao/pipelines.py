# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

import openpyxl
from itemadapter import ItemAdapter


class TaobaoPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = '电影'
        self.ws.append(('标签', '作者', '主题', '剧情'))

    def close_spider(self, spider):
        self.wb.save('电影.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        author = item.get('author', '')
        subject = item.get('subject', '')
        intro = item.get('intro', '')
        self.ws.append((title, author, subject, intro))
        return item


class SqlPipeline:
    def __init__(self):
        self.conn = sqlite3.Connection("test")  # 连接数据库
        self.c = self.conn.cursor()
        self.data = []
        # sql = '''create table name(title char,author char,subject char,intro char)
        # '''
        # self.c.execute(sql)

    def close_spider(self):
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        author = item.get('author', '')
        subject = item.get('subject', '')
        intro = item.get('intro', '')
        sql = '''insert into name(title,author,subject,intro) values ("%s","%s","%s","%s")
        ''' % (title, author, subject, intro)
        self.c.execute(sql)
        self.conn.commit()
        return item
