import sys,os
import subprocess
import urllib.request
import tarfile

p = os.listdir("/home/")

#for x in p:
    #print(x)
    #t = 'export JAVA_HOME=/home/'+x+'/Android'
    #subprocess.call(['echo',t,'>','file.txt'])
#projects_csv_fn = 'projects_csv_2.csv'
#prjects_json_fn = 'projects.json'
#args ='file.txt ' + prjects_json_fn + ' ' + projects_csv_fn
#subprocess.call(args, shell=True)
#def save(filename, contents):
    #fh = open(filename, 'w')
    #fh.write(contents)
    #fh.close()

#save('file.txt','Hello this is suresh')

#sam = "Hello this is fourth line"
#file = open("file.txt","a+")
#file.write("\n")
#file.write(sam)
print("Beginning Nagios download please wait...!")
#url = 'https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz'
#urllib.request.urlretrieve(url, 'release.tar.gz')
subprocess.call(['wget', '--no-check-certificate', '-O', 'nagios-plugins.tar.gz', 'https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz'])
print("Download is finished...! ")
print("extracting nagios please wait...!")
subprocess.call(['tar','xzf','nagios-plugins.tar.gz'])
#tar = tarfile.open("release.tar.gz")
#tar.extractall()
