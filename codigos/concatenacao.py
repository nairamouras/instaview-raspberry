from moviepy.editor import *
from moviepy.editor import VideoFileClip
from noticias import importacaoNoticias

#Função que concatena os clips criados com as imagens dos diretórios
def concatenaClips():
    fps = 30
    video = 'concatenados.mp4'
    clip_insta = VideoFileClip("clip-imagens-insta.mp4").margin(10)
    clip_dep = VideoFileClip('clip-imagens-dep.mp4').margin(10)
    clips = [[clip_insta, clip_dep]]
    final = clips_array(clips)
    #Salva o resultado da concatenação dos dois clips
    final.write_videofile(video, fps=fps)
    #Chamada para a importação das notícias
    importacaoNoticias()
    return