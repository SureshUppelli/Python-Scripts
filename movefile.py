import pwd
import grp
import os
#shutil.move("download.jpeg", "/home/suresh")
uid = pwd.getpwnam("apache").pw_uid
gid = grp.getgrnam("apache").gr_gid
print("Apache user id:",uid)
print("Apache group id:",gid)
#os.chown("/home/suresh/download.jpeg",)