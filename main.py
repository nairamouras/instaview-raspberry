import os
from datetime import date
from os import walk
import shutil
from importacaoInstagram import importacao
from webscraping import scrape
from reproducao import start
from radio import radio
from playlist import importacaoPlaylist

files = []
path = './ifmtcuiabaoficial'
video = 'completo_vinheta.mp4'
    
if (os.path.exists(path) == False):
    importacao()
else:
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break
    arq = os.path.join(path, files[0]) 
    fmt = '%d-%m-%Y'
    dataDoDiretorio = os.path.getmtime(arq)
    dataArquivo = date.fromtimestamp(dataDoDiretorio)
    dataHoje = date.today()
    quantidade_dias = abs((dataHoje - dataArquivo).days)
    if quantidade_dias >= 14:
        shutil.rmtree(path)
        importacao()
    else:
        scrape()

importacaoPlaylist()
radio()
start()
