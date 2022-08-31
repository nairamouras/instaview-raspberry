from os import walk
from moviepy.editor import *
import os
from webscraping import scrape
from loop_video import loop

def clips():
    files = []
    images_list = []
    videos_list = []
    path = './ifmtcuiabaoficial'
    video = 'completo.mp4'

    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break

    tamanho_files = len(files)

    for i in range(tamanho_files):
        if files[i].endswith('.jpg'):
            images_list.append(os.path.join(path, files[i]))
        elif files[i].endswith('.mp4'):
            videos_list.append(os.path.join(path, files[i]))
            
    fps = 30

    clips_image = [ImageClip(m).set_duration(7) for m in images_list]
        
    concat_clip_image = concatenate_videoclips(clips_image, method = 'compose')
    
    concat_clip_image.write_videofile('clip-imagens.mp4', fps=fps)

    tamanho_videos_list = len(videos_list)

    clips_video = [VideoFileClip(videos_list[c]) for c in range(tamanho_videos_list)]

    concat_clip_video = concatenate_videoclips(clips_video, method = 'compose')
    
    concat_clip_video.write_videofile('clip-videos.mp4', fps=fps)

    clip1 = VideoFileClip("clip-imagens.mp4").margin(10)

    clip2 = VideoFileClip("clip-videos.mp4").margin(10)

    clips = [[clip1, clip2]]

    final = clips_array(clips)
    
    final.write_videofile(video, fps=fps)

    loop()

    scrape()

