import urllib.request

def download(cookie, license, url, filename):
    print (url)
    print (filename)
    opener = urllib.request.build_opener()
    opener.addheaders.append((cookie, license))
    f = opener.open(url)
    with open(filename, 'wb') as save:
        save.write(f.read())

cookie = 'Cookie'
license = 'oraclelicense=accept-securebackup-cookie'
url = 'https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz'
filename = 'jdk-8u201-linux-x64.tar.gz'

download(cookie, license, url, filename)
#with lzma.open("/home/suresh/Downloads/node-v10.15.0-linux-x64.tar.xz") as f:
    #with tarfile.open(fileobj=f) as tar:
        #content = tar.extractall('/home/suresh/Music/')
        #print("Extracted...!")