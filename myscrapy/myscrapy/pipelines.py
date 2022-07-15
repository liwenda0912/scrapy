# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 钩子函数（方法）---》回调函数（方法）---》callback

# useful for handling different item types with a single interface
import sqlite3

import openpyxl


class sqlPipeline:  # 插入数据库
    def __init__(self):
        self.conn = sqlite3.connect("database")
        self.c = self.conn.cursor()
        self.data = []

    def closs_spiders(self, spider):
        if len(self.data) > 0:
            self.wirte()
        self.conn.close()

    def process_item(self, item, spider):
        name = str(item.get('title', ''))
        rank = str(item.get('rank', ''))
        subject = str(item.get('subject', ''))
        duration = str(item.get('duration', ''))
        intro = str(item.get('intro', ''))
        self.data.append((name, rank, subject, duration, intro))
        if len(self.data) == 50:
            self.wirte()
            self.data.clear()

        # sql = '''insert into move(title,评分,主题) values ("%s",%s,"%s")
        # ''' %(name,rank,subject)
        # self.c.execute(sql)

        self.conn.commit()
        return item

    def wirte(self):  # executemany出现数据库操作出现 near "%": syntax error错误使用？代替%S
        self.c.executemany(
            '''insert into test (title,评分,主题,时长,剧情) values (?,?,?,?,?)
    ''', self.data

        )


class MyscrapyPipeline:  # 生成xlsx文件
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'top250'
        self.ws.append(('标签', '评分', '主题', '时长', '剧情'))

    def open_spider(self, sider):
        pass

    def close_spider(self, spider):
        self.wb.save('data.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        duration = item.get('duration', '')
        intro = item.get('intro', '')
        self.ws.append((title, rank, subject, duration, intro))
        return item
