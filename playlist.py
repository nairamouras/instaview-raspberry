import wget

def importacaoPlaylist():
    file_url = 'https://player.hdradios.net/player/6990'
    file = 'listen.pls'
    wget.download(file_url , file )