import urllib.request
import os, sys

# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
print('Beginning slack download please wait...!')

#url = 'https://downloads.slack-edge.com/linux_releases/slack-desktop-3.3.3-amd64.deb'
#urllib.request.urlretrieve(url, '/home/suresh/Documents/slack2.deb')
print("Download is finished...!")