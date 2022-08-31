import os
import sys
import subprocess
import shlex

def TocaPlaylist():
    
    ComandoMPlayer = "mplayer -input file=/tmp/ControleRadio.txt -slave -playlist "
    Playlists=["https://player.hdradios.net/player-home-page/6990"]        
    NomesRadios=["Radio IFMT Campus Cuiaba"] 
 
    os.system("pkill -f mplayer")
    ComandoPlaylist = ComandoMPlayer + Playlists[0]
    FNULL = open(os.devnull,'w')
    args = shlex.split(ComandoPlaylist)
    InterfaceMPlayer = subprocess.Popen(args, shell=False, stdin=subprocess.PIPE, stdout=FNULL, stderr=subprocess.STDOUT)
    return

TocaPlaylist()