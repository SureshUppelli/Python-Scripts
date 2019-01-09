import urllib.request
import os, sys
import subprocess
# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
	print("Beginning Brackets download please wait...!")

	url = 'https://github.com/adobe/brackets/releases/download/release-1.13/Brackets.Release.1.13.64-bit.deb'
	urllib.request.urlretrieve(url, 'brackets.deb')
	print("Download is finished...!      Starting Installation        Please wait")
	#import subprocess
	subprocess.call(['dpkg','-i','brackets.deb'])
	subprocess.call(['apt','-f','install','-y'])
	print("Completed!")