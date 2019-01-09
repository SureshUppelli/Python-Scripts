import os
class myclass:
    print("Present Working Direcory is: "+os.getcwd())
    #print("Current Process ID is: " + os.getpid())
    if os.path.exists("/home/suresh/fie123"):
        print("File is Available")
    else:
        print("File is not available")
    print("Current login user:"+os.getlogin())
    for filename in os.listdir("/usr"):
        print("This is inside /tmp"+ filename)