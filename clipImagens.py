import asyncio
from asyncore import loop
from operator import concat
from os import walk
from moviepy.editor import *
import os
from webscraping import scrape

def clip():
    files = []
    images_list = []
    videos_list = []
    path = './ifmtcuiabaoficial'
    video = 'clips.mp4'

    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break

    tamanho_files = len(files)

    for i in range(tamanho_files):
        if files[i].endswith('.jpg'):
            images_list.append(os.path.join(path, files[i]))
        elif files[i].endswith('.mp4'):
            videos_list.append(os.path.join(path, files[i]))
            
    fps = 24

    print(images_list)

    clips_image = [ImageClip(m).set_duration(4) for m in images_list]
        
    concat_clip_image = concatenate_videoclips(clips_image, method = 'compose')

    tamanho_videos_list = len(videos_list)

    clips_video = [VideoFileClip(videos_list[c]) for c in range(tamanho_videos_list)]

    concat_clip_video = concatenate_videoclips(clips_video, method = 'compose')

    concat_all = concatenate_videoclips([concat_clip_video, concat_clip_image], method = 'compose')

    concat_all.write_videofile(video, fps=fps)
    
    scrape()
