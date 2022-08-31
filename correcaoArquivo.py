import os
from vinheta import vinheta

def correcao():
    file = open('noticias.csv', 'r')
    linhas = file.readlines()
            
    qtd = len(linhas)
    file.close()

    new_file = open('noticias-ifmt.csv', 'w')
    for i in range(qtd):
        if(i==0):
            new_file.writelines('')
        else:
            novas_linhas = linhas[i]+' | '
            new_file.writelines(novas_linhas)
    new_file.close()

    if os.path.exists('noticias.csv'):  
        os.remove('noticias.csv')

    vinheta()
