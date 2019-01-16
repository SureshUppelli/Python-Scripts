#import urllib.request
import os, sys
import subprocess


def check_service_status(service_name):
    status = os.system('systemctl status ' + service_name + ' > /dev/null')
    return status

def textReplace(old_txt,new_txt):
    # Read in the file
    with open('answer.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(old_txt, new_txt)

    # Write the file out again
    with open('answer.txt', 'w') as file:
        file.write(filedata)
def main():
        # if not root...kick out
    if not os.geteuid() == 0:
        sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
    else:
        print("Updating System")
        subprocess.call(['yum','-y','update'])
        print("Setting up RDO")
        subprocess.call(['yum', '-y', 'install', 'https://rdoproject.org/repos/rdo-release.rpm'])
        if (check_service_status("firewalld") == 0):
        	#print("Running")
            subprocess.call(['systemctl','disable','firewalld'])
            subprocess.call(['systemctl','stop','firewalld'])
        if (check_service_status("NetworkManager")==0):
            subprocess.call(['systemctl', 'disable', 'NetworkManager'])
            subprocess.call(['systemctl', 'stop', 'NetworkManager'])
        if not (check_service_status("network")==0):
            subprocess.call(['systemctl', 'enable', 'network'])
            subprocess.call(['systemctl', 'start', 'network'])
        subprocess.call(['yum','install','-y','openstack-packstack'])
        subprocess.call(['packstack','--gen-answer-file=/root/answer.txt'])
        os.chdir(r"/root/")
        passwd = "CONFIG_DEFAULT_PASSWORD="
	#swift = "CONFIG_SWIFT_INSTALL=y"
        clieo = "CONFIG_CEILOMETER_INSTALL=y"
        aodh = "CONFIG_AODH_INSTALL=y"
        provision = "CONFIG_PROVISION_DEMO=y"
        textReplace("CONFIG_DEFAULT_PASSWORD=", "Config_DEFAULT_PASSWORD=Novi1234")
        textReplace("CONFIG_SWIFT_INSTALL=y", "CONFIG_SWIFT_INSTALL=n")
        textReplace(clieo, "CONFIG_CEILOMETER_INSTALL=n")
        textReplace(aodh, "CONFIG_AODH_INSTALL=n")
        textReplace(provision,"CONFIG_PROVISION_DEMO=n")
        subprocess.call(['packstack', '--answer-file=answer.txt'])

main()

