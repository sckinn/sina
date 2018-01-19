# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["hq.sinajs.cn"]
    start_urls = [
        'http://hq.sinajs.cn/list=hk00001',
    ]

    def parse(self, response):
        item = {}
        item['info'] = response.text
        yield item
