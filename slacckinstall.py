import urllib.request
import os, sys
import subprocess
# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
	print("Beginning slack download please wait...!")

	url = 'https://downloads.slack-edge.com/linux_releases/slack-desktop-3.3.3-amd64.deb'
	url = 'https://downloads.slack-edge.com/linux_releases/slack-desktop-3.3.7-amd64.deb'
	urllib.request.urlretrieve(url, '/tmp/slack.deb')
	print("Download is finished...!      Starting Installation        Please wait")
	subprocess.call(['dpkg','-i','/tmp/slack.deb'])
	print("Completed!")
