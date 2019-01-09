import sys
import os
import subprocess


# If not root.. Kick out
if not os.getuid() == 0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
    print("Installing filezilla.. pleasse wiat!")
    subprocess.call(['apt','install','filezilla','-y'])
    print("Completed!")