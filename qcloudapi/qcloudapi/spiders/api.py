# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ['cloud.tencent.com']
    start_urls = ['https://cloud.tencent.com/document/api']

    def parse(self, response):
        for href in response.xpath('//a[@title="API 概览"]/@href'):
            yield response.follow(href, self.parse_api_page)
        for href in response.xpath('//a[@title="API概览"]/@href'):
            yield response.follow(href, self.parse_api_page)

    def parse_api_page(self,response):
        links = response.xpath('//table')
        for index,tbs in enumerate(links):
#             print(tbs)
            for ix,trs in enumerate(tbs.xpath('//tr')):
                yield {'data': trs.extract()}
