# -*- coding: utf-8 -*-
import scrapy
import json


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["dapp-beta2.degico.co","dapp.cloudapp.net","hq.sinajs.cn"]
    start_urls = [
        #'https://dapp-beta2.degico.co/hkgdstock/getsrcurls',
        'https://dapp.cloudapp.net/hkgdstock/getsrcurls',
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        for u in jsonresponse:
            yield scrapy.Request(u, callback=self.parse_sina)

    def parse_sina(self, response):
        item = {}
        item['info'] = response.text
        yield item
