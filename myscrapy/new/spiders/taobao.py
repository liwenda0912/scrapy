import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from lxml import etree
import json
from new.items import NewItem
from concurrent.futures import ThreadPoolExecutor


class TaobaoSpider(scrapy.Spider):
    start_urls = ["https://www.taobao.com"]
    name = 'taobao'
    allows_domains = ['www.taobao.com']

    def parse(self, response, **kwargs, ):
        der = webdriver.Chrome(executable_path='chromedriver')
        der.get(response.url)
        der.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        page_html = der.page_source
        data = etree.HTML(page_html)
        move = NewItem()
        t = data.xpath(
            '//div/div[@class="tb-recommend-content-item"]/a/div[@class="info-wrapper"]')
        for i in t:
            text = i.xpath('div[@class="title"]/text()')
            move['text'] = text[0]
            yield move

        der.close()  # 关闭浏览器
        der.quit()  # 退出浏览器
# 保存writer中的数据至excel
# 如果省略该语句，则数据不会写入到上边创建的excel文件中
