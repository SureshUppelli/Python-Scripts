import sys
import os
import subprocess
#import tarfile
import urllib.request

if not os.getuid() == 0:
    sys.exit("nYou must be root to run this application, please    use sudo and try again.\n")
else:
    print("Please wait while installing Nodejs 10 ! ")
    subprocess.call(['curl', '-sL', 'https://deb.nodesource.com/setup_10.x', '|', 'sudo', '-E', 'bash', '-'])
    subprocess.call(['sudo', 'apt-get', 'install', '-y', 'nodejs'])
    print("Nodejs is installed ")
    print("Installing react-native !")
    subprocess.call('npm', 'install', '-g', 'react-native-cli')
    print("React native is installed.")