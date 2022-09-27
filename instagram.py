from instaloader import Instaloader, Profile
from datetime import datetime, timedelta
from pastaIFMT import correcaoPasta

#Função responsável por executar o download das imagens do Instagram Oficial do IFMT
def importacaoInstagram():
    #Ele realiza o download das imagens dos últimos 5 dias
    data_inicio = datetime.today() - timedelta(days=5)
    L=Instaloader()
    PROFILE = 'ifmtcuiabaoficial'
    profile = Profile.from_username(L.context, PROFILE)
    post_sorted = sorted(profile.get_posts(),key=lambda post: post.likes, reverse=True)
    for post in post_sorted:
        if post.date >= data_inicio or post.is_pinned:
            L.download_post(post,PROFILE)
    #Chamada para a função de correção da pasta com os arquivos do Instagram
    correcaoPasta()
    return
