import os,sys
import subprocess
import urllib.request
import tarfile

def textReplace(old_txt,new_txt):
    # Read in the file
    with open('/etc/selinux/config', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(old_txt, new_txt)
    # Write the file out again
    with open('/etc/selinux/config', 'w') as file:
        file.write(filedata)

def installPrerequisites():
    subprocess.call(['yum','-y','install','gcc','glibc-common','wget', 'unzip','httpd', 'php', 'gd', 'gd-devel', 'perl', 'postfix'])

#Dowloading Nagios 4.4.3
def downloadNagios():
    os.chdir(r"/tmp/")
    print("Beginning Nagios download please wait...!")
    url = 'https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.4.3.tar.gz'
    urllib.request.urlretrieve(url, 'nagioscore.tar.gz')
    print("Download is finished...!")
    tar = tarfile.open("nagioscore.tar.gz")
    tar.extractall()
    print("extracting nagios please wait...!")

def installNagios():
    os.chdir(r"/tmp/nagioscore-nagios-4.4.3")
    subprocess.call(['./configure'])
    subprocess.call(['make','all'])
    subprocess.call(['make','install-groups-users'])
    subprocess.call(['usermod','-a','-G','nagios','apache'])
    subprocess.call(['make','install'])

def main():

    # if not root...kick out
    if not os.geteuid() == 0:
        sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
    else:
        textReplace("SELINUX=enforcing","SELINUX=disabled")
        installPrerequisites()
        downloadNagios()
        installNagios()


main()