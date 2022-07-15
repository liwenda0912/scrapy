import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from myscrapy.items import ItemTest


class DoubanSipder(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(1):
            yield scrapy.Request(
                url=f'https://movie.douban.com/top250?start={25 * i}&filter=',
                # 代理 meta={'proxy': 'socks5://127.0.0.1:6023'}
            )
            # request是proxies = { ’http://.1.1.1:8585‘
            # }

    def parse(self, response: HtmlResponse, **kwargs):
        data = Selector(response)
        re = data.css('#content>div>div.article>ol>li')
        for i in re:
            detail_url = i.css('div.info>div.hd>a::attr(href)').extract_first()
            move = ItemTest()
            move['title'] = i.css('span.title::text').extract_first()
            move['rank'] = i.css('span.rating_num::text').extract_first()
            move['subject'] = i.css('span.inq::text').extract_first()

            yield Request(url=detail_url, callback=self.parse_detail, cb_kwargs={'item': move})

    def parse_detail(self, response, **kwargs):
        sel = Selector(response)
        move = kwargs['item']
        move['duration'] = sel.css('span[property="v:runtime"]::attr(content)').extract_first()
        move['intro'] = sel.css('span[property="v:summary"]::text').extract_first()
        yield move
