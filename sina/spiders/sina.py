# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["hq.sinajs.cn"]
    start_urls = [
        'http://hq.sinajs.cn/list=hk00001',
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u)