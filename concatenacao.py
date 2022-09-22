from moviepy.editor import *
from moviepy.editor import VideoFileClip
from vinheta import criaVinheta

#Função que concatena os clips criados com as imagens dos diretórios
def concatenaClips(video_insta, video_dep):
    fps = 30
    video = 'concatenados.mp4'
    clip_dep = VideoFileClip(video_dep).margin(10)
    clip_insta = VideoFileClip(video_insta).margin(10)
    clips = [[clip_insta, clip_dep]]
    final = clips_array(clips)
    #Salva o resultado da concatenação dos dois clips
    final.write_videofile(video, fps=fps)
    #Chamada para a criação da vinheta
    criaVinheta('concatenados.mp4')
    return