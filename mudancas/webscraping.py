import requests
from bs4 import BeautifulSoup
import pandas as pd
from correcaoArquivo import correcao

def scrape():
    lista_noticias = []

    response = requests.get('https://cba.ifmt.edu.br/inicio/')

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('div', attrs = {'class':"row padding-left"})

    for noticia in noticias:

        titulo = noticia.find('p', attrs= {'class':"no-margin espacamento-medio"})
        
        lista_noticias.append([titulo.text])

    news = pd.DataFrame(lista_noticias)

    news.to_csv('noticias.csv', index=False)
    
    correcao()
