import urllib.request
#import tarfile
import os
import sys
import subprocess

#if not root.. kock out
if not os.getuid() == 0:
    sys.exit("nYou must be root to run this application, please    use sudo and try again.\n")
else:
    print("Please wait while Downloading and Installing nodejs....\n")
    url = 'https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz'
    urllib.request.urlretrieve(url,'nodejs.tar.xz')
    print("Extracting nodejs")
    #tr = tarfile.open("node-v10.14.2-linux-x64.tar.xz")
    #tr.extractall()
    subprocess.call(['sudo','tar','-xJf','nodejs.tar.xz'])
    print("Completed!")