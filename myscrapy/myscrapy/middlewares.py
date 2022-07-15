# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


def get_cookies():
    cookies = 'Cookie: ll="118286"; bid=yt8xzIGexSQ; _vwo_uuid_v2=D297D75F9076980802A7234104C2DC11F|7b7c1f18e2b8fdd881d1fcdf989261a1; __gads=ID=815c09e79ca9ab9b-22a675a6a8d30011:T=1654072353:RT=1654072353:S=ALNI_MbbDLxSxZB-I6FZacEl2QNKJ3OgXQ; __utmz=30149280.1654149376.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1654149376.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=DIBhQBYWxtovuBrElSulOndqpcjp2Z5K; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1654517671%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXphquqnT6InmtaovIy9XqpgHTAJoVHj2NBAxHvIbXzIDLuPN3fFbn-qlZ3k487n2%26wd%3D%26eqid%3Db58b0a520012724a00000006629850fc%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1353865167.1653892606.1654319391.1654517671.6; __utmb=30149280.0.10.1654517671; __utmc=30149280; __utma=223695111.298837651.1653892606.1654319391.1654517671.6; __utmb=223695111.0.10.1654517671; __utmc=223695111; __gpi=UID=00000616b6916c2d:T=1654072353:RT=1654517671:S=ALNI_MYB24bwJSQ8S8LiLvtlMk-iTSao-w; dbcl2="257722684:6s6hXChzHWw"; ck=W2En; _pk_id.100001.4cf6=4bb3a81fca4a1b69.1653892605.6.1654517739.1654319391.; push_noty_num=0; push_doumail_num=0'
    cookies_dict = {}
    for i in cookies.split(';'):
        key, value = i.split('=', maxsplit=1)
        cookies_dict[key] = value
        return cookies_dict


COOKIES = get_cookies()


class MyscrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyscrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        request.cookies = COOKIES
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
