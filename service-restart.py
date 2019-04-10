# This one is required, but should already be installed
#sudo apt-get install python-gobject

# Installing this will install the
# notify-send program. Check that out
# for sending notifications in the shell
#sudo apt-get install libnotify-bin

# The development headers if you
# want to do any development in C/C++
#sudo apt-get install libnotify-dev




import sys,os
import subprocess
from gi.repository import Notify


def check_service_status(service_name):
    status = os.system('systemctl status ' + service_name + ' > /dev/null')
    return status

if (check_service_status("ngios") != 0):
    Notify.init("App Name")
    Notify.Notification.new("SSH Service is not runnng").show()

