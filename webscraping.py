from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd
from correcaoArquivo import correcao

def scrape():
    #criando uma lista para guardar os conteúdos das noticias 
    lista_noticias = []

    response = requests.get('https://cba.ifmt.edu.br/inicio/')

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('div', attrs = {'class':"row padding-left"})

    for noticia in noticias:

        # titulo da noticia
        titulo = noticia.find('p', attrs= {'class':"no-margin espacamento-medio"})

        #print(titulo.text)

        #Salvando os conteúdos em uma lista
        lista_noticias.append([titulo.text])

    news = pd.DataFrame(lista_noticias)

    news.to_csv('noticias.csv', index=False)

    #print(lista_noticias)
    
    correcao()
