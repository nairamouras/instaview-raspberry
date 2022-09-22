import wget
import os

#Função responsável pelo download da playlist da rádio
def importacaoPlaylist():
    playlist = 'playlist.pls'
    #Exclui a playlist anterior, se existir
    if(os.path.exists(playlist)):
        os.remove(playlist)
    #URL da playlist Web Rádio do IFMT
    file_url = 'https://player.hdradios.net/player/6990'
    wget.download(file_url , playlist)
    return