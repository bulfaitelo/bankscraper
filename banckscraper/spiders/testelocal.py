# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest

class TestelocalSpider(scrapy.Spider):
    name = 'testelocal'
    allowed_domains = ['mediaserver/custodia']
    start_urls = ['http://mediaserver/custodia/']

    def parse(self, response):
        seguimentos = response.xpath(
            '//div[contains(@class, "box-custodia")]'
        )
        # self.log(seguimentos)
        for custodias in seguimentos:
            custodia = custodias.xpath('./a[contains(@class, "link-acoes")]')
            custodia_name = custodia.xpath("text()").extract_first()
            custodia_value = custodia.xpath("./span/text()").extract_first()
            
            self.log("Nome: %s - Valor: %s" % (custodia_name, custodia_value))
            
            # tabelas = custodias.xpath('//div/')
            # /html/body/div[3]/div[3]/section/div/div[5]/div/table/tbody
            # /html/body/div[3]/div[3]/section/div/div[4]/div/table/tbody/tr[1]/td[8]
            ativos = custodias.xpath("./div/table/tbody/tr")
            if ativos:                                
                for ativo in ativos:
                    # self.log("==> "+ativo.xpath('./td/a/text()').extract_first()+" Valor: "+ativo.xpath('./td[8]/a/text()').extract_first())
                    # /html/body/div[3]/div[3]/section/div/div[4]/div/table/tbody/tr[2]/td[8]
                    self.log("==> %s  Valor: %s" %(ativo.xpath('./td/a/text()').extract_first(), ativo.xpath('./td[8]/text()').extract_first()))
            # if :
            #     itens = custodia.xpath('//table[contains(@class, "table-easy")]/tbody/tr/td')
            #     for investimentos in itens:
            #         self.log(investimentos)