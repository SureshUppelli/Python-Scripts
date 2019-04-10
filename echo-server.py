import urllib
from urllib.request import urlopen

def download(cookie, license, url, filename):
    print (url)
    print (filename)
    opener = urllib.build_opener()
    opener.addheaders.append((cookie, license))
    f = opener.open(url)
    with open(filename, 'wb+') as save:
        save.write(f.read())

cookie = 'Cookie'
license = 'oraclelicense=accept-securebackup-cookie'
url = 'https://download.oracle.com/otn-pub/java/jdk/8u202-b08/1961070e4c9b4e26a04e7f5a083f551e/jdk-8u202-linux-x64.tar.gz'
filename = 'jdk-8u202-linux-x64.tar.gz'

download(cookie, license, url, filename)