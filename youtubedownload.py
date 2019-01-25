#from pytube import YouTube
#yt = YouTube("https://www.youtube.com/watch?v=28EfGCmaCP0")
#yt = yt.get('mp4', '720p')
#yt.download('/home/suresh/Music')

from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('/home/suresh/Music')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=28EfGCmaCP0'])