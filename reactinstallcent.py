import urllib.request
import lzma
import tarfile
from distutils.dir_util import copy_tree
from contextlib import closing
import os,sys,subprocess



if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
# Downloading node js form local server
    print("Downloading nodejs please wait...!")
    url = 'ftp://192.168.0.115/pub/node-v10.15.0-linux-x64.tar.xz'
    urllib.request.urlretrieve(url, 'node-v10.15.0-linux-x64.tar.xz')
    print("Downloading Finished...!")
    with lzma.open("node-v10.15.0-linux-x64.tar.xz") as f:
        with tarfile.open(fileobj=f) as tar:
            content = tar.extractall('.')
            print("Extracted...!")


#copy subdirectory example
    fromDirectory = "node-v10.15.0-linux-x64/bin/"
    toDirectory = "/usr/"
    copy_tree(fromDirectory, toDirectory)

    fromDirectory = "node-v10.15.0-linux-x64/include/"
    toDirectory = "/usr/"
    copy_tree(fromDirectory, toDirectory)

    fromDirectory = "node-v10.15.0-linux-x64/lib/"
    toDirectory = "/usr/"
    copy_tree(fromDirectory, toDirectory)

    fromDirectory = "node-v10.15.0-linux-x64/share/"
    toDirectory = "/usr/"
    copy_tree(fromDirectory, toDirectory)

#Downloading JDK 8 from local server
    print("Downloading jdk 8 please wait...!")
    url = 'ftp://192.168.0.115/pub/jdk-8u201-linux-x64.tar.gz'
    urllib.request.urlretrieve(url, 'jdk-8u201-linux-x64.tar.gz')
    print("Downloading Finished...!")
    tf = tarfile.open("jdk-8u201-linux-x64.tar.gz")
    tf.extractall()
    print("Extraced...!")
    fromDirectory = "jdk1.8.0_201"
    toDirectory = "/opt/"
    copy_tree(fromDirectory, toDirectory)
    print("Installing react-native ... please wait!")
    subprocess.call(['npm','install','react-native-cli'])

    p = os.listdir("/home/")
    for x in p:
        print(x[0])
        t = 'export JAVA_HOME=/home/' + x + '/Android'

        subprocess.call(['echo',t,'>>','/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'PATH =$PATH:$ANDROID_HOME / emulator', '>>', '/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'PATH =$PATH:$ANDROID_HOME / tools', '>>', '/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'PATH =$PATH:$ANDROID_HOME / tools / bin', '>>', '/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'PATH =$PATH:$ANDROID_HOME / platform - tools', '>>', '/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'JAVA_HOME =/opt/jdk1.8.0_201', '>>', '/home/x/.bashrc'])
        subprocess.call(['echo', 'export', 'PATH =$JAVA_HOME/bin:$PATH', '>>', '/home/x/.bashrc'])
