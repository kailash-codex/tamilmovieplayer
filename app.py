from moviepy.editor import VideoFileClip
import pymediainfo
import time

m3u8_link = 'D2786.mp4.m3u8'

media_info = pymediainfo.MediaInfo.parse(m3u8_link)
for track in media_info.tracks:
    if track.track_type == 'Video':
        url = track.url
        clip = VideoFileClip(url)
        clip.preview()
        