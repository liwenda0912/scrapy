# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class NewPipeline:
    def __init__(self):
        self.conn = sqlite3.Connection('text')
        self.c = self.conn.cursor()
        # sql = '''create table data(text)
        # '''
        # self.conn.execute(sql)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        data = item.get('text', '')
        d = data.split('"')
        sql = '''insert into data(text) values ("%s")
        ''' % (d[0],)
        self.conn.execute(sql)
        self.conn.commit()
        return item
