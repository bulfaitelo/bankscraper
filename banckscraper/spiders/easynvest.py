# -*- coding: utf-8 -*-
import scrapy

class EasynvestSpider(scrapy.Spider):
    name = 'easynvest'
    # allowed_domains = ['www.easynvest.com.br', 'portal.easynvest.com.br']
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
        print("After login Titulo: %s" % response.xpath('//title/text()').extract_first())
        yield scrapy.Request(
            url='https://portal.easynvest.com.br/financascustodia/rendafixa/',
            callback=self.parse_tesouro_direto,            
        )
    def parse_tesouro_direto(self, response):
        ativos_tesouro =  response.xpath(
            '//tbody/tr'
        )
        for ativo in ativos_tesouro:
            nome_ativo = ativo.xpath('./td[1]/a/text()').extract_first()
            nome_emissor = ativo.xpath('./td[2]/text()').extract_first()
            quantidade = ativo.xpath('./td[3]/text()').extract_first()
            investimento = ativo.xpath('./td[4]/text()').extract_first()
            vencimento = ativo.xpath('./td[5]/text()').extract_first()
            taxa_negociada = ativo.xpath('./td[6]/text()').extract_first()
            ir_iof_taxa = ativo.xpath('./td[7]/text()').extract_first()
            Valor = ativo.xpath('./td[8]/text()').extract_first()            
            print(" %s, %s, %s, %s, %s, %s, %s, %s, "% (nome_ativo, nome_emissor, quantidade, investimento, vencimento, taxa_negociada, ir_iof_taxa, Valor))
        
