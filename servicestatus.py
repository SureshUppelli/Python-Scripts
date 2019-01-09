import os
#import commands


service_name = "mysql"

def check_service_status(service_name):

        status = os.system('systemctl status ' +service_name+ ' > /dev/null')
        return status

def main():

        if (check_service_status("sshd") == 0):
                print ("Running")
        else:
                print ("Stopped")
main()
