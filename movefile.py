import pwd
import grp
import os
#shutil.move("download.jpeg", "/home/suresh")
uid = pwd.getpwnam("apache").pw_uid
gid = grp.getgrnam("apache").gr_gid
print("Apache user id:",uid)
print("Apache group id:",gid)
#os.chown("/home/suresh/download.jpeg",)


# Read in the file
        with open('/etc/selinux/config', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('SELINUX=enforcing', 'SELINUX=disabled')

        # Write the file out again
        with open('/etc/selinux/config', 'w') as file:
            file.write(filedata)