import vlc
import time

player = vlc.Instance()
media_list = player.media_list_new()
media_player = player.media_list_player_new()
media = player.media_new('vinheta.mp4')
media_list.add_media(media)
media_player.set_media_list(media_list)
player.vlm_set_loop('vinheta', True)

media_player.play()