import os
from os import walk
from clips import criaClips

#Função responsável por corrigir a falha de download dos arquivos .mp4
def correcaoPasta():
    files = []
    path = 'ifmtcuiabaoficial'
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break
    tamanho = len(files)
    for i in range(tamanho):
        #Se existir um arquivo .mp4, ele busca o arquivo .jpg com o mesmo nome
        if files[i].endswith('.mp4'):
            aux = os.path.splitext(files[i])
            auxi = []
            for j in range(tamanho):
                if files[j].endswith('.jpg'):
                    auxi = os.path.splitext(files[j])
                    #Se existir um arquivo .jpg (frame inicial do .mp4), ele é excluído
                    if auxi[0] == aux[0]:
                        lix = os.path.join(path, files[j])
                        if os.path.isfile(files[j]) == False:
                            os.remove(lix)
                            aux = []
                    auxi = []
    #Após a correção, inicia a chamada para a criação dos primeiros clips de vídeo
    criaClips()
