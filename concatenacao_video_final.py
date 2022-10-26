from moviepy.editor import *
import os
#import vinheta

def concatenacao_final():
    fps = 30
    path = 'videos'
    videos = []
    video = 'video_final.mp4'
    clips = []
    i = 0
    for video in os.listdir(path):
        videos.append((os.path.join(path, video)))
    tamanho = len(videos)
    for i in range(tamanho):
        clips.append(VideoFileClip(videos[i]))
    final = concatenate_videoclips(clips, method = 'compose')
    final.write_videofile(video, fps=fps)
    #Chama a função de criação da vinheta
    #vinheta.cria_vinheta(video)