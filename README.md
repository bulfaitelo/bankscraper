# Bankscraper

A ideia inicial é criar uma ferramenta par afazer a raspagem dos dados de alguns bancos, inicialmente criarei para o Easynvest e posteriormente para o Santander, conforme for para outros. 

## Requerimentos Scrapy
#### Install:
```sh
pip install scrapy
```

Depois é só clonar o repositório entrar no Banksraper e rodar o comando:
```sh
scrapy crawl easynvest -a ac_number=xxxxxx -a password=xxxxxxx
```

#### Onde
**ac_number** é o número da sua conta de acesso
**password**  é sua senha (não o token de transação, nunca use esse token em aplicações de terceiros 

*Em breve mais informações*
