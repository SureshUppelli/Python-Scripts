#from shutil import copyfile
import sys
import os
import subprocess
import shutil
#import tarfile
import urllib.request
class reactNative:
    def installReactNative(self):
        #if not root.. kick out
        if not os.getuid() == 0:
            sys.exit("nYou must be root to run this application, please    use sudo and try again.\n")
        else:
            print("Please wait while Downloading and Installing nodejs....")
            url = 'https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz'
            urllib.request.urlretrieve(url, 'nodejs.tar.xz')
            print("Extracting nodejs")
            subprocess.call(['sudo', 'tar', '-xJf', 'nodejs.tar.xz'])
            #copyfile('node-v10.14.2-linux-x64/include','/usr/')
            #copyfile('node-v10.14.2-linux-x64/lib', '/usr/')
            #copyfile('node-v10.14.2-linux-x64/include', '/usr/')
            shutil.copy('node-v10.14.2-linux-x64/','/usr/')
            #shutil.copy('node-v10.14.2-linux-x64/include', '/usr/')
            #shutil.copy('node-v10.14.2-linux-x64/lib', '/usr/')
            #shutil.copy('node-v10.14.2-linux-x64/share', '/usr/')

            ('node-v10.14.2-linux-x64/share', '/usr/')
            print("Completed!")

rn = reactNative()
rn.installReactNative()