# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 爬取到的数据需要组装成item
class ItemTest(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()
    duration = scrapy.Field()
    intro = scrapy.Field()


