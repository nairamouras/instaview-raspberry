import os
import shutil
from instagram import importacaoInstagram
from noticias import importacaoNoticias
import vlc
from playlist import importacaoPlaylist
from github import exclusaoRepo, importacaoGit

path_instagram = 'ifmtcuiabaoficial'
video = 'concatenados_final.mp4'
path_dep = 'dep'

if os.path.exists('clip-imagens-insta.mp4'):  
    os.remove('clip-imagens-insta.mp4')
if os.path.exists('clip-imagens-dep.mp4'):  
    os.remove('clip-imagens-dep.mp4')
if os.path.exists('concatenados_final.mp4'):  
    os.remove('concatenados_final.mp4')

importacaoPlaylist()
importacaoNoticias()
exclusaoRepo(path_dep)
importacaoGit()
if(os.path.exists(path_instagram)):
    shutil.rmtree(path_instagram)
importacaoInstagram()

os.system("sudo shutdown -r 06:00")

doTrashCode = False

video_player = vlc.MediaPlayer(video)
media_player = vlc.MediaListPlayer()
playlist_player = vlc.Instance()

def start():
    media_list = playlist_player.media_list_new()
    media = playlist_player.media_new('playlist.pls')
    media_list.add_media(media)
    media_player.set_media_list(media_list)
    media_player.play()
    video_player.set_fullscreen(False)
    em = video_player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    video_player.play()

def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True

def back():
    video_player.set_media(video_player.get_media())
    video_player.play()

start()

while media_player.is_playing:
    if doTrashCode:
        back()
        doTrashCode = False
