from moviepy.editor import *

path = 'completo.mp4'
video = VideoFileClip(path)
audio = AudioFileClip(path)
audio = afx.audio_loop(audio, duration = video.duration)
clip1 = VideoFileClip(path)
clip1 = vfx.loop(clip1, n = 3, duration = video.duration)
clip1 = clip1.set_audio(audio)
clip1.write_videofile("loop.mp4")