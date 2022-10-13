from moviepy.editor import *
from moviepy.editor import VideoFileClip
import os

def concatenaFinal():
    fps = 30
    path = 'videos'
    videos = []
    clips = []
    i = 0
    for video in os.listdir(path):
        videos.append((os.path.join(path, video)))
    tamanho = len(videos)
    for i in range(tamanho):
        clips.append(VideoFileClip(videos[i]))
    final = concatenate_videoclips(clips, method = 'compose')
    final.write_videofile('concatenados_final.mp4', fps=fps)
    #Chamada para a criação da vinheta
    #criaVinheta(video)
    return