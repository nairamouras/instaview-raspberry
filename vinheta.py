from moviepy.editor import VideoFileClip, ColorClip, TextClip, CompositeVideoClip

def vinheta():
    
    video = VideoFileClip('loop.mp4')

    f = open('noticias-ifmt.csv', 'r')
    data = f.read().replace('\n', '')

    text = TextClip(data, color = 'white',font = "Arial", fontsize = 80
        ).set_duration(video.duration)

    color = ColorClip(
        text.size, color = (0, 128, 0), duration = video.duration
    )

    cor_texto = CompositeVideoClip([color, text]).set_position(pos)

    compose = CompositeVideoClip([video, cor_texto])

    compose.write_videofile('completo_vinheta.mp4')

def pos(time):
        return(time*-250, 'bottom')
