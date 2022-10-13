from moviepy.editor import *
from moviepy.editor import VideoFileClip
import os
from concatenacao2 import concatenaFinal
#from vinheta import criaVinheta

#Função que concatena os clips criados com as imagens dos diretórios
def concatenaClips(video_insta, video_dep):
    fps = 30
    video = 'concatenados_insta_dep.mp4'
    path = 'videos'
    if video_insta == None:
        clip_dep = VideoFileClip(video_dep)
        clips = clip_dep.resize((1200,800))
        clips.write_videofile(os.path.join(path, video), fps=fps)
    elif video_dep == None:
        clip_insta = VideoFileClip(video_insta)
        clips = clip_insta.resize((1200,800))
        clips.write_videofile(os.path.join(path, video), fps=fps)
    else:
        clip_dep = VideoFileClip(video_dep).margin(10)
        clip_insta = VideoFileClip(video_insta).margin(10)
        clips = [[clip_insta, clip_dep]]
        final = clips_array(clips)
        #Salva o resultado da concatenação dos dois clips
        final.write_videofile(os.path.join(path, video), fps=fps)
    concatenaFinal()
    return