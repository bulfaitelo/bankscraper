# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash


class EasynvestSpider(scrapy.Spider):
    name = 'easynvest'
    allowed_domains = ['www.easynvest.com.br', 'portal.easynvest.com.br']
    start_urls = [
        'https://portal.easynvest.com.br/autenticacao/login'
    ]


    def parse(self, response):
        return scrapy_splash.SplashFormRequest.from_response(
            response,
            formdata={'Conta': self.ac_number, 'AssinaturaEletronica': self.password},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        # self.log(response.xpath('//title/text()').extract_first())
        yield scrapy_splash.SplashRequest(
            splash_url='https://portal.easynvest.com.br/financas/custodia/',
            callback=self.parse_custodia
        )
    def parse_custodia(self, response):
        seguimentos = response.xpath(
            '//div[contains(@class, "box-custodia")]'
        )
        self.log(seguimentos)





        # for custodias in seguimentos:
        #     custodia = custodias.xpath('./a[contains(@class, "link-acoes")]')
        #     custodia_name = custodia.xpath("text()").extract_first()
        #     custodia_value = custodia.xpath("./span/text()").extract_first()
            
        #     self.log("Nome: %s - Valor: %s" % (custodia_name, custodia_value))
            
        #     # tabelas = custodias.xpath('//div/')
        #     # /html/body/div[3]/div[3]/section/div/div[5]/div/table/tbody
        #     # /html/body/div[3]/div[3]/section/div/div[4]/div/table/tbody/tr[1]/td[8]
        #     ativos = custodias.xpath("./div/table/tbody/tr")
        #     if ativos:                                
        #         for ativo in ativos:
        #             # self.log("==> "+ativo.xpath('./td/a/text()').extract_first()+" Valor: "+ativo.xpath('./td[8]/a/text()').extract_first())
        #             # /html/body/div[3]/div[3]/section/div/div[4]/div/table/tbody/tr[2]/td[8]
        #             self.log("==> %s  Valor: %s" %(ativo.xpath('./td/a/text()').extract_first(), ativo.xpath('./td[8]/text()').extract_first()))
            
            
            
            
            
            
            
            
            
            
            
            
            # if :
            #     itens = custodia.xpath('//table[contains(@class, "table-easy")]/tbody/tr/td')
            #     for investimentos in itens:
            #         self.log(investimentos)
        

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