# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
      'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
      'Crawler.comm.rotate_useragent.RotateUserAgentMiddleware' :400
}
