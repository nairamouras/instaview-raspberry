from moviepy.editor import *

#Cria um pré loop do vídeo com a vinheta
def loop():
    path = 'com-vinheta.mp4'
    video = VideoFileClip(path)
    clip1 = VideoFileClip(path)
    #Define 2 repetições
    clip1 = vfx.loop(clip1, n = 2, duration = video.duration)
    #Salva o resultado
    clip1.write_videofile("videoFinal.mp4")
    return