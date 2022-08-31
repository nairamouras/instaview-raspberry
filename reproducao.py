
import vlc


doTrashCode = False
player = vlc.MediaPlayer("completo_vinheta.mp4")


def start():
    player.set_fullscreen(True)
    em = player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    player.play()


def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True


def back():
    player.set_media(player.get_media())
    player.play()

while True:
    if doTrashCode:
        back()
        doTrashCode = False