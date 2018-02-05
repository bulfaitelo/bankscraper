# -*- coding: utf-8 -*-
import scrapy


class EasynvestExtratoSpider(scrapy.Spider):
    name = 'easynvest_extrato'
    # allowed_domains = ['www.easynvest.com.br', 'portal.easynvest.com.br']
    start_urls = ['http://portal.easynvest.com.br/autenticacao/login/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'Conta': self.ac_number, 'AssinaturaEletronica': self.password},
            callback=self.after_login
        )
    # Redirecionando para XHR dos rendimentos do tesouro direto. 
    def after_login(self, response):
        # check login succeed before going on
        print("After login Titulo: %s" % response.xpath('//title/text()').extract_first())
        yield scrapy.Request(
            url='https://portal.easynvest.com.br/financas/extrato/',
            callback=self.parse_extrato,            
        )
    def parse_extrato(self, response):
        # Extrato
        extrato =  response.xpath(
            '//table[contains(@class, "table-easy")]/tbody/tr'
        )
        print("After login Titulo: %s" % response.xpath('//title/text()').extract_first())
        for extrato_detalhado in extrato:
            liquidacao = extrato_detalhado.xpath('./td[1]/text()').extract_first()
            movimentacao = extrato_detalhado.xpath('./td[2]/text()').extract_first()
            historico = extrato_detalhado.xpath('./td[3]/text()').extract_first()
            lancamento = extrato_detalhado.xpath('./td[4]/text()').extract_first()
            saldo = extrato_detalhado.xpath('./td[5]/text()').extract_first()
            print("%s, %s, %s, %s, %s, " % (liquidacao, movimentacao, historico, lancamento, saldo))
    
