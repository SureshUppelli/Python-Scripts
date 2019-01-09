import sys
import os
import subprocess
#import tarfile
import urllib.request

class reactNative:
    def installReactNative(self):
        #if not root.. kick out
        if not os.getuid() == 0:
            sys.exit("nYou must be root to run this application, please    use sudo and try again.\n")
        else:
            print("Please wait while Downloading and Installing nodejs....\n")
            #url = 'https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz'
            #urllib.request.urlretrieve(url,'/temp/nodejs.tar.xz')
            #print("Extracting tar file")
            #tr = tarfile.open("/tmp/nodejs.tar.xz")
            #tr.extractall()
            #subprocess.call(['sudo', 'tar', '-xJf', '/temp/nodejs.tar.xz'])
            #print("Completed!")
            print("Please wait while Downloading and Installing nodejs....\n")
            url = 'https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz'
            urllib.request.urlretrieve(url, 'nodejs.tar.xz')
            print("Extracting nodejs")
            # tr = tarfile.open("node-v10.14.2-linux-x64.tar.xz")
            # tr.extractall()
            subprocess.call(['sudo', 'tar', '-xJf', 'nodejs.tar.xz'])
            print("Completed!")
            subprocess.call(['sudo','cp','-rf','node-v10.14.2-linux-x64/bin','/usr/'])

            subprocess.call(['cp', '-rf', '/tmp/nodejs/node-v10.14.2-linux-x64/include', '/usr/'])
            subprocess.call(['cp', '-rf', '/tmp/nodejs/node-v10.14.2-linux-x64/lib', '/usr/'])
            subprocess.call(['cp', '-rf', '/tmp/nodejs/node-v10.14.2-linux-x64/share', '/usr/'])
            subprocess.call(['rm', '-rf', 'node*'])
            print (subprocess.call(['node','-v']))
            #print("Downloading OpenJdk 1.8")
            #url = "https://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz"
            #urllib.request.urlretrieve(url,"/opt/openJdk1.8.tar.gz")
            #print("Extracting openJdk file")
            #subprocess.call(['sudo', 'tar', '-xzf', '/opt/openJdk1.8.tar.gz'])
            #print("Completed!")
            #print ("Setting up Android and Java Environment variable")
            #subprocess.call(['rm','openJdk1.8'])
            #subprocess.call(['echo','export JAVA_HOME=/opt/openJdk1.8','>>','~/.bashrc'])
            #subprocess.call(['echo','export PATH=$JAVA_HOME/bin:${PATH}','>>','~/.bashrc'])
            #ubprocess.call(['echo','export ANDROID_HOME=$HOME/Android/Sdk','>>','~/.bashrc'])
            #subprocess.call(['echo','export PATH=$PATH:$ANDROID_HOME/emulator','>>','~/.bashrc'])
            #ubprocess.call(['echo','export PATH=$PATH:$ANDROID_HOME/tools','>>','~/.bashrc'])
            #subprocess.call(['echo','export PATH=$PATH:$ANDROID_HOME/tools/bin','>>','~/.bashrc'])
            #subprocess.call(['echo', 'export PATH=$PATH:$ANDROID_HOME/platform-tools','>>', '~/.bashrc'])
            #print("Please wait while installing react-native....!")
            #subprocess.call(['npm','install','-g','react-native-cli'])
            #subprocess.call(['adb'])
            #print("Completed!")


#Creating object for reactNative Class and calling installReactNative function
install = reactNative()
install.installReactNative()