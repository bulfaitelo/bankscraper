# Bankscraper

A ideia inicial é criar uma ferramenta par afazer a raspagem dos dados de alguns bancos, inicialmente criarei para o Easynvest e posteriormente para o Santander, conforme for para outros. 

## Requerimentos Scrapy
#### Install:
```sh
pip install scrapy
```

Depois é só clonar o repositório entrar no Banksraper e rodar o comando:

###### Listar os ativos: 
```sh
scrapy crawl easynvest_ativos -a ac_number=xxxxxx -a password=xxxxxxx
```

###### Listar o extrato do mes vigente: 
```sh
scrapy crawl easynvest_extrato -a ac_number=xxxxxx -a password=xxxxxxx
```

Caso não queira ver os logs adicione o parametro ``--nolog``



#### Onde
**ac_number** é o número da sua conta de acesso

**password**  é sua senha (não o token de transação, nunca use esse token em aplicações de terceiros 

*Em breve mais informações*
