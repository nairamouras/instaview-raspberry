from moviepy.editor import VideoFileClip, ColorClip, TextClip, CompositeVideoClip
import os

#Função que retorna a velocidade e a posição da vinheta no vídeo
def pos(time):
    return (time*-350, 'bottom')
#Função que cria a vinheta, concatena e salva com o vídeo dos clips
def criaVinheta(arq):
    path = 'videos'
    video = VideoFileClip(arq)
    duracao = video.duration
    #Abre o novo arquivo .csv apenas para leitura
    f = open('noticias-ifmt.csv', 'r')
    data = f.read().replace('\n', '')
    #Cria um clip de texto
    text = TextClip(
        data, color = 'white',font = 'Arial', fontsize = 80
        ).set_duration(duracao)
    #Cria um clip de cor
    color = ColorClip(
        text.size, color = (0, 128, 0), duration = duracao
    )
    #Concatena ambas os clips e definem sua posição no vídeo
    cor_texto = CompositeVideoClip([color, text]).set_position(pos)
    compose = CompositeVideoClip([video, cor_texto])
    #Salva o resultado
    compose.write_videofile(os.path.join(path, 'com-vinheta.mp4'))
