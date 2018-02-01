# -*- coding: utf-8 -*-
import scrapy

class EasynvestSpider(scrapy.Spider):
    name = 'easynvest'
    allowed_domains = ['www.easynvest.com.br', 'portal.easynvest.com.br']
    start_urls = [
        'https://portal.easynvest.com.br/autenticacao/login'
    ]


    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'Conta': self.ac_number, 'AssinaturaEletronica': self.password},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        # self.log(response.xpath('//title/text()').extract_first())
        yield scrapy.Request(
            url = 'https://portal.easynvest.com.br/financas/custodia/',
            callback=self.parse_custodia
        )
    def parse_custodia(self, response):
        seguimentos = response.xpath(
            '//div[contains(@class, "box-custodia")]'
        )
        self.log(seguimentos)
        for custodias in seguimentos:
            custodia = custodias.xpath('./a[contains(@class, "link-acoes")]/text()').extract_first()            
            self.log(custodia)
        

    # def parse(self, response):     
        # formdata = {
        #     'Conta': self.ac_number,
        #     'AssinaturaEletronica': self.password
        # }
        # self.log(formdata)
        # headers = response.headers
        
        # self.log(cookies)
        # auth_token = ''
        # for cookie in cookies:
        #     cookie = cookie.decode('utf-8')
        #     if 'AuthToken' in cookie:
        #         auth_token = cookie.split(';')[0].split('=')[1]
        #         break
        # self.log(auth_token)       
        
        # yield scrapy.FormRequest(
        #     url='https://portal.easynvest.com.br/autenticacao/login/', 
        #     method='POST', formdata=formdata, callback=self.parse_login,
        #     headers=headers
        # )
    # def parse_login(self, response):        
    #     yield scrapy.Request(
    #         url='https://portal.easynvest.com.br/Financas',
    #         callback=self.parse_finance
    #     )
    # def parse_finance(self, response):
    #     self.log(response.xpath('//title/text()').extract_first())