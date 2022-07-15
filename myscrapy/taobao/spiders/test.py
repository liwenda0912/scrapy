import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from taobao.items import TaobaoItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allows_domains = ['www.qidian.com']
    start_urls = ["https://www.qidian.com/rank/yuepiao/"]

    def parse(self, response: HtmlResponse, **kwargs):
        data = Selector(response)
        re = data.css('div.book-img-text>ul>li')
        for i in re:
            detail_url = i.css('a[data-eid="qd_C39"]::attr(href)').extract_first()
            move = TaobaoItem()
            move['title'] = i.css("h2>a::text").extract_first()
            move['author'] = i.css('p.author>a.name::text').extract_first()
            move['subject'] = i.css('p.author>a[data-eid="qd_C42"]::text').extract_first()
            move['intro'] = i.css("p.intro::text").extract_first()
            yield Request(url='https:' + detail_url + '/', callback=self.parse_de_, cb_kwargs={'item': move},
                          dont_filter=True)

    def parse_de_(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        move = kwargs['item']
        move['name'] = sel.css('meta::text').extract_first()
        print(move['name'])
        yield move
