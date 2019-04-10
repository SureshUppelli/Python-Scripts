import urllib.request
import os, sys
import subprocess
# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
	print("Beginning slack download please wait...!")

	#url = 'http://dl.google.com/android/studio/install/0.3.2/android-studio-bundle-132.893413-linux.tgz'
	#urllib.request.urlretrieve(url, '/tmp/slack.deb')
	#print("Download is finished...!      Starting Installation        Please wait")
	#import subprocess
	#subprocess.call(['dpkg','-i','/tmp/slack.deb'])

	print("Completed!")
