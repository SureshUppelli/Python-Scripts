import urllib.request
import os, sys
import subprocess
# if not root...kick out
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
	print("Beginning Visual Studio code download please wait...!")

	url = 'https://az764295.vo.msecnd.net/stable/dea8705087adb1b5e5ae1d9123278e178656186a/code_1.30.1-1545156774_amd64.deb'
	urllib.request.urlretrieve(url, 'vscode.deb')
	print("Download is finished...!      Starting Installation        Please wait")
	#import subprocess
	subprocess.call(['dpkg','-i','vscode.deb'])
	#subprocess.call(['apt','-f','install','-y'])
	print("Completed!")
