import os, sys
import subprocess
import pymysql
import random
import string
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM = "suresh.uppapalli@gmail.com"


def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """Your mail reader does not support the report format. Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
    #
    # Credentials (if needed) for sending the mail

    server.starttls()

    server.login(FROM, getpass.getpass())
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

    return print("mail sent")


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


def textoverride(rand):
    f = open("/home/user1/Downloads/nimmigration/properties.ini", "w")
    text = "host =192.168.0.97\ndbname =nimmigrationtest\nuser =root\npassword =" + rand + "\ntype =mysql"
    f.write(text)
    f.close()

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
             py_mail("Subject", rand, "jyothin@novisync.com", FROM)
             textoverride(rand)
main()