import urllib.request
import os, sys
import subprocess


def check_service_status(service_name):
    status = os.system('systemctl status ' + service_name + ' > /dev/null')
    return status
main():

    # if not root...kick out
    if not os.geteuid() == 0:
        sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
    else:
        print("Updating System")
        subprocess.call(['yum','-y','update'])
        print("Setting up RDO")
        subprocess.call(['rpm', '-y', 'https://rdoproject.org/repos/rdo-release.rpm'])
        if (check_service_status("firewalld") == 0):
        #print("Running")
            subprocess.call(['systemctl','disable','firewalld'])
            subprocess.call(['systemctl','stop','firewalld'])
        if (check_service_status("NetworkManager")==0):
            subprocess.call(['systemctl', 'disable', 'NetworkManager'])
            subprocess.call(['systemctl', 'stop', 'NetworkManager'])
        if (check_service_status("network")!=0):
            subprocess.call(['systemctl', 'enable', 'network'])
            subprocess.call(['systemctl', 'start', 'network'])
        subprocess.call(['yum','install','-y','openstack-packstack'])
        subprocess.call(['packstack','--gen-answer-file=/root/answer.txt'])
