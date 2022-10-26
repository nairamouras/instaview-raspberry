from moviepy.editor import *
import os
import concatenacao_video_final

#Função que concatena os clipes criados com as imagens dos diretórios
def concatenacao_clipes(video_insta, video_git):
    fps = 30
    video = 'clips_concatenados.mp4'
    path = 'videos'
    if video_insta == None:
        clipe_git = VideoFileClip(video_git)
        clipes = clipe_git.resize((1200,800))
        clipes.write_videofile(os.path.join(path, video), fps=fps)
    elif video_git == None:
        clipe_insta = VideoFileClip(video_insta)
        clipes = clipe_insta.resize((1200,800))
        clipes.write_videofile(os.path.join(path, video), fps=fps)
    else:
        clipe_git = VideoFileClip(video_git).margin(10)
        clipe_insta = VideoFileClip(video_insta).margin(10)
        clipes = [[clipe_insta, clipe_git]]
        final = clips_array(clipes)
        #Salva o resultado da concatenação dos dois clipes
        final.write_videofile(os.path.join(path, video), fps=fps)
    concatenacao_video_final.concatenacao_final()