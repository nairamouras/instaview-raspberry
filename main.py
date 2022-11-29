import os
import shutil
import instagram
#import noticias
import vlc
import playlist
import github
import ctypes

#Função que inicia a reprodução do vídeo e da playlist da rádio
def start():
    ctypes.CDLL('libX11.so.6').XInitThreads()
    media_player = vlc.MediaListPlayer()
    playlist_player = vlc.Instance()
    media_list = playlist_player.media_list_new()
    media = playlist_player.media_new('playlist.pls')
    media_list.add_media(media)
    media_player.set_media_list(media_list)
    media_player.play()
    video_player.set_fullscreen(True)
    em = video_player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    video_player.play()

#Função responsável por verificar se a reprodução do video está chegando ao fim
def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True

#Função responsável por iniciar o vídeo novamente, ativando o loop
def back():
    video_player.set_media(video_player.get_media())
    video_player.play()

if __name__ == '__main__':
    
    #Executa um comando no terminal para minimizar a tela
    comando = 'xdotool getactivewindow'
    shell = os.popen(comando)
    codigo_tela = str(shell.read())
    os.system('xdotool windowminimize ' + codigo_tela)

    path_instagram = 'ifmtcuiabaoficial'
    video = 'video_final.mp4'
    path_git = 'github'
    path_videos = 'videos'

    #Exclui todos os vídeos criados anteriormente para não ocorrer conflitos
    if os.path.exists('clipe-imagens-insta.mp4'):  
        os.remove('clipe-imagens-insta.mp4')
    if os.path.exists('clipe-imagens-git.mp4'):  
        os.remove('clipe-imagens-git.mp4')
    if os.path.exists('video_final.mp4'):  
        os.remove('video_final.mp4')
    if os.path.exists(path_videos):  
        shutil.rmtree(path_videos)
    os.mkdir(path_videos)

    #Chama a função de download da playlist da rádio
    playlist.download_playlist()
    #Chama a função de raspagem dos títulos de notícias do site
    #noticias.scraping_noticias()
    #Chama a função que exclui o diretório local do GitHub clonado anteriormente
    github.exclui_repositorio(path_git)
    #Chama a função para clonar o repositório remoto
    github.git_clone()

    #Se existir, exclui a pasta do Instagram e realiza um novo download
    if os.path.exists(path_instagram):
        shutil.rmtree(path_instagram)
    instagram.download_instagram()

    #Define um horário para a reinicialização do sistema
    os.system("sudo shutdown -r 06:00")

    doTrashCode = False

    video_player = vlc.MediaPlayer(video)

    start()

    #Loop de reprodução do vídeo e da playlist
    while True:
        if doTrashCode:
            back()
            doTrashCode = False
