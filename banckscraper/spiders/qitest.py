# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_splash import SplashFormRequest

class QitestSpider(scrapy.Spider):
    name = 'qitest'
    start_urls = ['http://qiestudo.bulfaitelo.dyndns.info:1010/login']


    def parse(self, response):
        return SplashFormRequest.from_response(
            response,
            formdata={'email': self.email, 'password': self.password},
            callback=self.after_login   
        )

    def after_login(self, response):
        print(response.xpath('//title/text()').extract_first())
        yield SplashRequest(
            url='http://qiestudo.bulfaitelo.dyndns.info:1010/quest/questionnaires/create',
            callback=self.parse_create,
        )

    def parse_create(self, response):
        print("Depois do Login:   %s" % response.xpath('//title/text()').extract_first())

        
        


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