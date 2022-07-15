import requests
from lxml import html

etree = html.etree
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
url = 'https://movie.douban.com/top250'
response = requests.get(url=url, headers=headers)
data = response.text

et = etree.HTML(data)
title = et.xpath("//div/div[@class='article']/ol/li//div/a/span[@class='title']/text()")
rank = et.xpath("//div/div[@class='article']/ol/li//div[@class='star']/span[@class='rating_num']/text()")
subject = et.xpath("//div/div[@class='article']/ol/li//div/p/span/text()")
print(title)
