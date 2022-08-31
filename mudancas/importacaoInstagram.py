from instaloader import Instaloader, Profile
from datetime import datetime, timedelta
from correcaoPastaIfmt import correcao

def importacao():
    data_inicio = datetime.today() - timedelta(days=14)
    L=Instaloader()

    PROFILE = "ifmtcuiabaoficial"
    profile =Profile.from_username(L.context, PROFILE)
    post_sorted = sorted(profile.get_posts(),key=lambda post: post.likes, reverse=True)

    for post in post_sorted:
        if post.date > data_inicio:
            L.download_post(post,PROFILE)
    
    correcao()

