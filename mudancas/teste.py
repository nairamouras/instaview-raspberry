
import subprocess
import vlc

player = vlc.MediaPlayer('completo_vinheta.mp4')
p = subprocess.Popen('cvlc', 'fullscreen', 'home/pi/demo.mp4', '--loop')
player.play()

