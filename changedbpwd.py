import os, sys
import subprocess
import pymysql
import random
import string



def randomStringDigits(stringlength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringlength))


def check_service_status(service_name):
    status = os.system('systemctl status ' + service_name + ' > /dev/null')
    return status
#https://stackoverflow.com/questions/33510184/change-mysql-root-password-on-centos7


def dbcreation(rand):
    con = pymysql.connect(host='localhost', user='root', password='')
    print("connected to database")
    try:
       with con.cursor() as cursor:

        #sql = "UPDATE mysql.user SET authentication_string = PASSWORD(%s) WHERE User = 'root' AND Host = 'localhost';", rand
        cursor.execute("UPDATE mysql.user SET authentication_string = PASSWORD(%s) WHERE User = 'root' AND Host = 'localhost';", rand)
               #perm = "grant all on nextclouddb.* to 'root'@'localhost' identified by '';"
        #flush = "FLUSH PRIVILEGES;"
                #cursor.execute(perm)
        cursor.execute("FLUSH PRIVILEGES;")
        #warn = "ALTER USER 'root'@'localhost' IDENTIFIED BY %s;", rand
        cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY %s;", rand)
    finally:
        con.close()


def main():

    # if not root...kick out
    if not os.geteuid() == 0:
        sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
    else:
        # if check_service_status("mysqld")  returns 0 then stop mysqld service
         if(check_service_status("mysqld") == 0):
             subprocess.call(['systemctl', 'stop', 'mysqld'])
             subprocess.call(['systemctl', 'set-environment','MYSQLD_OPTS="--skip-grant-tables"'])
             subprocess.call(['systemctl', 'start', 'mysqld'])
             rand = randomStringDigits(14)
             print("Password is :"+rand)
             dbcreation(rand)
             print("Mysql Password Changed")
             subprocess.call(['systemctl', 'stop', 'mysqld'])
             subprocess.call(['systemctl', 'unset-environment', 'MYSQLD_OPTS'])
             subprocess.call(['systemctl', 'start', 'mysqld'])
main()