from moviepy.editor import VideoFileClip, ColorClip, TextClip, CompositeVideoClip

def vinheta():
    
    video = VideoFileClip('./clips.mp4')

    f = open('noticias-ifmt.csv', 'r')
    data = f.read().replace('\n', '')

    text = TextClip(data, color = 'green', fontsize = 80
        ).set_duration(video.duration)

    color = ColorClip(
        text.size, color = (255, 255, 255), duration = video.duration
    )

    cor_texto = CompositeVideoClip([color, text]).set_position(pos)

    compose = CompositeVideoClip([video, cor_texto])

    compose.write_videofile('vinheta.mp4')

def pos(time):
        return(time*-250, 'bottom')