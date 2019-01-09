import urllib.request
import os, sys
import subprocess
# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
    print()