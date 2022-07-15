import scrapy
from scrapy import Selector

from myscrapy.items import ItemTest


class XpathScrapy(scrapy.Spider):
    name = 'xpath'
    allows_domains = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):
            yield scrapy.Request(url=f'https://movie.douban.com/top250?start={25 * page}&filter=')

    def parse(self, response):
        move = ItemTest()
        data = Selector(response)
        title = data.xpath("//div/div[@class='article']/ol/li//div/a/span[@class='title'][1]/text()").extract()
        num =len(title)
        rank = data.xpath("//div/div[@class='article']/ol/li//div[@class='star']/span["
                          "@class='rating_num']/text()").extract()
        subject = data.xpath("//div/div[@class='article']/ol/li//div/p/span/text()").extract()
        for i in range(num):
            print(i)
            move['title'] = title[i]
            move['rank'] = rank[i]
            move['subject'] = subject[i]
            yield move
