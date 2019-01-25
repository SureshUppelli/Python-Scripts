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


#Installing Pre-requisites
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


def installDaemon():
    subprocess.call(['make','install-daemoninit'])
    subprocess.call(['systemctl','enable','httpd.service'])
    subprocess.call(['make','install-commandmode'])
    subprocess.call(['make','install-config'])
    subprocess.call(['make', 'install-webconf'])
    subprocess.call(['firewall-cmd', '--zone=public', '--add-port=80/tcp'])
    subprocess.call(['firewall-cmd', '--zone=public', '--add-port=80/tcp','--permanent'])


#Installing Nagios Plugins From Source
def installPlugins():
    os.chdir(r"/tmp/")
    subprocess.call(['yum', 'install', '-y', 'gcc', 'glibc', 'glibc-common', 'make', 'gettext', 'automake', 'autoconf', 'wget', 'openssl-devel', 'net-snmp', 'net-snmp-utils', 'epel-release'])
    subprocess.call(['yum', 'install', '-y', 'perl-Net-SNMP'])
    #Downloading Plugin Source
    subprocess.call(['wget', '--no-check-certificate', '-O', 'nagios-plugins.tar.gz',
                     'https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz'])
    print("Download is finished...! ")
    print("extracting nagios please wait...!")
    subprocess.call(['tar', 'xzf', 'nagios-plugins.tar.gz'])

    #Compile and Install
    os.chdir(r"/tmp/nagios-plugins-release-2.2.1/")
    subprocess.call(['./tools/setup'])
    subprocess.call(['./configure'])
    subprocess.call(['make'])
    subprocess.call(['make', 'install'])
    print("Nagios Plugin installation is completed !")
    subprocess.call(['systemctl', 'restart', 'nagios.service'])
    print("Nagios service is restart and ready to use")


def main():

    # if not root...kick out
    if not os.geteuid() == 0:
        sys.exit("\nYou must be root to run this application, please use su and try again.\n")
    else:
        pwd = input("Enter password for nagiosadmin\n")
        textReplace("SELINUX=enforcing","SELINUX=disabled")
        installPrerequisites()
        downloadNagios()
        installNagios()
        installDaemon()
        subprocess.call(['htpasswd','-b', '-c', '/usr/local/nagios/etc/htpasswd.users', 'nagiosadmin', pwd])
        subprocess.call(['systemctl', 'start', 'httpd.service'])
        subprocess.call(['systemctl', 'start', 'nagios.service'])
        installPlugins()



main()