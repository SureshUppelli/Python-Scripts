
# install pip using sudo apt-get install python3-pip
#sudo pip install --upgrade pip
#sudo pip install youtube_dl

from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('/home/suresh/Music')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=28EfGCmaCP0'])