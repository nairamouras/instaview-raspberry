from os import walk
from moviepy.editor import *
import os
from concatenacao import concatenaClips()
from noticias import importacaoNoticias

#Função responsável por criar os primeiros clips de vídeo, das imagens da pasta do Instagram e da pasta dos departamentos
def criaClips():
    files_insta = []
    files_dep = []
    images_list_insta = []
    images_list_dep = []
    path_pasta_instagram = './ifmtcuiabaoficial'
    path_pasta_dep = './teste'
    qtd_imagens_insta = 0
    qtd_imagens_dep = 0
    tempo_base = 5
    fps = 30
    for (dirpath, dirnames, filenames_insta) in walk(path_pasta_instagram):
        files_insta.extend(filenames_insta)
        break
    tamanho_files_insta = len(files_insta)
    #Cria uma lista com as imagens da pasta do Instagram
    for i in range(tamanho_files_insta):
        if files_insta[i].endswith('.jpg'):
            qtd_imagens_insta+=1
            images_list_insta.append(os.path.join(path_pasta_instagram, files_insta[i]))
        else:
            pass
    for (dirpath, dirnames, filenames_dep) in walk(path_pasta_dep):
        files_dep.extend(filenames_dep)
        break
    tamanho_files_dep = len(files_dep)
    #Cria uma lista com as imagens da pasta dos departamentos
    for i in range(tamanho_files_dep):
        if files_dep[i].endswith('.jpg'):
            qtd_imagens_dep+=1
            images_list_dep.append(os.path.join(path_pasta_dep, files_dep[i]))
        else:
            pass
    #Se a quantidade de imagens do Instagram for maior, elas que irão definir o tempo de duração do vídeo (tempo_base*qtd_imagens_insta)
    #E cada imagem dos departamentos terá uma duração definida pelo produto entre a quantidade de vezes que é menor e o tempo base (5 segundos)
    if(qtd_imagens_insta > qtd_imagens_dep):
        div = (qtd_imagens_insta)/(qtd_imagens_dep)
        tempo_insta = tempo_base
        tempo_dep = tempo_base*div
    else:
    #Se a quantidade de imagens dos departamentos for maior, elas que irão definir o tempo de duração do vídeo (tempo_base*qtd_imagens_dep)
    #E cada imagem do Instagram terá uma duração definida pelo produto entre a quantidade de vezes que é menor e o tempo base (5 segundos)
        div = (qtd_imagens_dep)/(qtd_imagens_insta)
        tempo_dep = tempo_base
        tempo_insta = tempo_base*div
    if tamanho_files_dep > 0:
        #Cria um clip com as imagens do Instagram, definindo seu tempo de tela
        clips_image_insta = [ImageClip(m).set_duration(tempo_insta) for m in images_list_insta]  
        concat_clip_image_insta = concatenate_videoclips(clips_image_insta, method = 'compose')
        #Salva o clip
        concat_clip_image_insta.write_videofile('clip-imagens-insta.mp4', fps=fps)
        #Cria um clip com as imagens dos departamentos, definindo seu tempo de tela
        clips_image_dep = [ImageClip(n).set_duration(tempo_dep) for n in images_list_dep] 
        concat_clip_image_dep = concatenate_videoclips(clips_image_dep, method = 'compose')
        #Salva o clip
        concat_clip_image_dep.write_videofile('clip-imagens-dep.mp4', fps=fps)
        #Chamada da função responsável por concatenar os clips criados
        concatenaClips()
    else:
        #Cria um clip com as imagens do Instagram, definindo seu tempo de tela
        clips_image_insta = [ImageClip(m).set_duration(tempo_insta) for m in images_list_insta]  
        concat_clip_image_insta = concatenate_videoclips(clips_image_insta, method = 'compose')
        #Salva o clip
        concat_clip_image_insta.write_videofile('clip-imagens-insta.mp4', fps=fps)
        #Chamada para a importação das notícias
        importacaoNoticias()
    return