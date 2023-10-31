from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import math


url = 'https://www.kabum.com.br/computadores/notebooks'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', id='listingCount').get_text().strip()


index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pag = math.ceil(int(qtd)/20)

dic_products = {'marca': [], 'preço': []}

for i in range(1, ultima_pag+1):
    url_pag = f'https://www.kabum.com.br/computadores/notebooks?page_number={i}2&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))
    
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        
        print(marca, preco)
        
        dic_products['marca'].append(marca)
        dic_products['preço'].append(preco)
        
        print(url_pag)
        
        
df = pd.DataFrame(dic_products)
df.to_csv('c:\\Users\\moyse\\Desktop\\Web_Scrapping\\Web_Scrapping\\Web_Scrapping\\notebook_gamer.csv', encoding='utf-8', sep=';')

        


