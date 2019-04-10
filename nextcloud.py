import subprocess,os,sys
import urllib.request
import shutil
import pwd
import grp
import pymysql
import pymysql.cursors
class nextcloud:
    def epelrepo(self):
        subprocess.call(['rpm','-ivh','https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'])
        subprocess.call(['rpm','-ivh','https://mirror.webtatic.com/yum/el7/webtatic-release.rpm'])
    def apache(self):
        subprocess.call(['yum','install','-y','httpd','wget','bzip2'])
    def php7(self):
        subprocess.call(['yum','install','-y','php71w','php71w-common','php71w-gd','php71w-intl','php71w-mbstring','php71w-mcrypt','php71w-mysqlnd','php71w-process','php71w-xml','php71w-cli','php71w-pdo'])
        subprocess.call(['yum','install','-y','mysql-server','mysql'])
    def nextcloud(self):
        os.chdir(r"/tmp")
        print("Starting NextCloud Download")
        url = "https://download.nextcloud.com/server/releases/latest.tar.bz2"
        urllib.request.urlretrieve(url,"latest.tar.bz2")
        print("Dowload is completed")
        subprocess.call(['tar', '-jxvf', 'latest.tar.bz2'])
        shutil.move("latest/nextcloud", "/var/www/html/")
        os.mkdir("/var/www/html/nextcloud/data")
        uid = pwd.getpwnam("apache").pw_uid
        gid = grp.getgrnam("apache").gr_gid
        os.chown("/var/www/html/nextcloud/",uid,gid)
        subprocess.call(['systemctl','start','httpd'])
        subprocess.call(['systemctl','start','mariadb'])
        subprocess.call(['systemctl','enable','httpd'])
        subprocess.call(['systemctl','enable','mariadb'])
    def dbcreation(self):
        con = pymysql.connect(host='localhost', user='root', password='')
        print("connected to database")
        try:
            with con.cursor() as cursor:
                sql = "create database nextclouddb;"
                cursor.execute(sql)
                perm = "grant all on nextclouddb.* to 'root'@'localhost' identified by '';"
                cursor.execute(perm)
        finally:
            con.close()
    def selinux(self):
        # Read in the file
        with open('/etc/selinux/config', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('SELINUX=enforcing', 'SELINUX=disabled')

        # Write the file out again
        with open('/etc/selinux/config', 'w') as file:
            file.write(filedata)
    def firewall(self):
        subprocess.call(['systemctl','stop','firewalld'])
        subprocess.call(['systemctl','disable','firewalld'])


if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
    nc = nextcloud()
    nc.selinux()
    nc.firewall()
    nc.epelrepo()
    nc.apache()
    nc.php7()
    nc.nextcloud()
    nc.dbcreation()