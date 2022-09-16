import os
from datetime import date
import shutil
from instagram import importacaoInstagram
from noticias import importacaoNoticias
import time
import vlc
from playlist import importacaoPlaylist

files = []
path_instagram = './ifmtcuiabaoficial'
video = 'com-vinheta.mp4'
doTrashCode = False
video_player = vlc.MediaPlayer(video)
media_player = vlc.MediaListPlayer()
playlist_player = vlc.Instance()
#Chamada para a função de download da playlist da rádio e imagens do Instagram
importacaoPlaylist()
#Apaga a pasta antiga do Instagram, se existir
if(os.path.exists(path_instagram)):
    shutil.rmtree(path_instagram)
importacaoInstagram()
#Função de start da reprodução do vídeo e da rádio
def start():
    media_list = playlist_player.media_list_new() 
    media = playlist_player.media_new('playlist.pls') 
    media_list.add_media(media) 
    media_player.set_media_list(media_list) 
    media_player.play()
    #Delay de 2 segundos antes de reproduzir o vídeo
    time.sleep(2)  
    video_player.set_fullscreen(True)
    em = video_player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    video_player.play()
    return
def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True
    return
#Função para reiniciar a reprodução do vídeo
def back():
    video_player.set_media(video_player.get_media())
    video_player.play()
    return
#Inicia a rádio e o vídeo antes de entrar definitivamente no loop infinito
start()
#Enquanto a rádio estiver tocando, o vídeo será reproduzido em loop
while media_player.is_playing():
    if doTrashCode:
        back()
        doTrashCode = False