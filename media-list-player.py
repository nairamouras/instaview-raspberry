import os
import vlc

videos = []
path_videos = 'videos'
doTrashCode = False

for vid in os.listdir(path_videos):
    videos.append(os.path.join(path_videos, vid))

video_player = vlc.MediaListPlayer()
playlist_videos_player = vlc.Instance()
video_list = playlist_videos_player.media_list_new()
media_player = vlc.MediaListPlayer()
playlist_player = vlc.Instance()
i = 0
tamanho = len(videos)

def start():
    global i
    media_list = playlist_player.media_list_new()
    media = playlist_player.media_new('playlist.pls') 
    media_list.add_media(media) 
    media_player.set_media_list(media_list) 
    media_player.play()
    for vid in videos:
        video = playlist_videos_player.media_new(vid)
        video_list.add_media(video)
        video_player.set_media_list(video_list)
    new_player = video_player.get_media_player()
    new_player.set_fullscreen(True)
    em = new_player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    video_player.play_item_at_index(0)
    i+=1
    return

def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True
    return

def back():
    global i
    if i <= tamanho-1:
        video_player.next()
        i+=1
    else:
        video_player.play_item_at_index(0)
        i = 0
    return
start()

while media_player.is_playing:
    if doTrashCode:
        back()
        doTrashCode = False