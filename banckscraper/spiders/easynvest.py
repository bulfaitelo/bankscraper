# -*- coding: utf-8 -*-
import scrapy


class EasynvestSpider(scrapy.Spider):
    name = 'easynvest'
    allowed_domains = ['easynvest.com.br']
    start_urls = ['http://easynvest.com.br/']

    def parse(self, response):
        pass
