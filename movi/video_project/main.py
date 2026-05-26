from moviepy import *

clip1 = ImageClip("gold.webp").with_duration(27)
clip2 = ImageClip("phone reayalme.webp").with_duration(27)
clip3 = ImageClip("t sart.webp").with_duration(27)
clip4 = ImageClip("tarck ball.webp").with_duration(27)

video = concatenate_videoclips([clip1, clip2, clip3,clip4])

text = TextClip(
    text=" ",
    font_size=70,
    color="white"
).with_duration(120).with_position("center")

final_video = CompositeVideoClip([video, text])

audio = AudioFileClip("Serge_Quadrado_-_Festival.mp3").subclipped(0, 108)

final_video = final_video.with_audio(audio)

final_video.write_videofile(
    "my_final_video.mp4",
    fps=24
)