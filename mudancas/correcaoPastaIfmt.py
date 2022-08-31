import os
from os import walk
from clipImagens import clips

def correcao():
    files = []
    path = './ifmtcuiabaoficial'

    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break

    tamanho = len(files)

    for i in range(tamanho):
        if files[i].endswith('.mp4'):
            aux = os.path.splitext(files[i])
            auxi = []
            print(aux)
            for j in range(tamanho):
                if files[j].endswith('.jpg'):
                    auxi = os.path.splitext(files[j])
                    if auxi[0] == aux[0]:
                        lix = os.path.join(path, files[j])
                        if os.path.isfile(files[j]) == False:
                            print(lix)
                            os.remove(lix)
                            aux = []
                    auxi = []
    clips()
