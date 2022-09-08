import vlc 
import time 
media_player = vlc.MediaListPlayer() 
player = vlc.Instance() 
media_list = player.media_list_new() 
media = player.media_new("listen.pls") 
media_list.add_media(media) 
media_player.set_media_list(media_list) 
  
  
media_player.play() 
time.sleep(5) 
value = media_player.is_playing() 
print(value) 
