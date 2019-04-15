import subprocess,os,sys
import urllib.request
import shutil
import pwd
import grp
import pymysql
import pymysql.cursors
class nextcloud:
    def epelrepo(self):
        subprocess.call(['yum','update','-y'])
        subprocess.call(['rpm','-ivh','https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'])
        subprocess.call(['rpm','-ivh','https://mirror.webtatic.com/yum/el7/webtatic-release.rpm'])

    def apache(self):
        subprocess.call(['yum','install','-y','httpd','wget','bzip2'])
    def php7(self):
        subprocess.call(['yum','install','-y','php71w','php71w-common','php71w-gd','php71w-intl','php71w-mbstring','php71w-mcrypt','php71w-mysqlnd','php71w-process','php71w-xml','php71w-cli','php71w-pdo'])
        subprocess.call(['yum','install','-y','mariadb-server','mysql'])
    def nextcloud(self):
        os.chdir(r"/tmp")
        print("Starting NextCloud Download")
        url = "https://download.nextcloud.com/server/releases/latest.tar.bz2"
        urllib.request.urlretrieve(url,"latest.tar.bz2")
        #subprocess.call(['wget','wget https://download.nextcloud.com/server/releases/latest.tar.bz2'])
        print("Dowload is completed")
        subprocess.call(['tar','-jxvf','latest.tar.bz2'])
        shutil.move("nextcloud", "/var/www/html/")
        os.mkdir("/var/www/html/nextcloud/data")
        #uid = pwd.getpwnam("apache").pw_uid
        #gid = grp.getgrnam("apache").gr_gid
        #os.chown("/var/www/html/nextcloud/",uid,gid)
        subprocess.call(['chown','-R','apache:apache','/var/www/html/nextcloud'])
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
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/data'])
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/config(/.*)?'])
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/apps(/.*)?'])
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/3rdparty(/.*)?'])
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/.htaccess'])
        subprocess.call(['semanage', 'fcontext', '-a', '-t', 'httpd_sys_rw_content_t', '/var/www/html/nextcloud/.user.ini'])
        subprocess.call(['restorecon', '-Rv', '/var/www/html/nextcloud/'])
    def firewall(self):
        subprocess.call(['firewall-cmd', '--permanent', '--add-service=http'])
        subprocess.call(['firewall-cmd','--permanent', '--add-service=https'])
        subprocess.call(['firewall-cmd', '--reload'])
        subprocess.call(['iptables', '-I', 'INPUT', '-p', 'tcp', '-m', 'tcp', '--dport', '80', '-j', 'ACCEPT'])
        subprocess.call(['iptables', '-I', 'INPUT', '-p', 'tcp', '-m', 'tcp', '--dport', '443', '-j', 'ACCEPT'])
        subprocess.call(['service', 'iptables','save'])


if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")
else:
    #Creating Object for nextcloud and calling its functions
    nc = nextcloud()
    nc.epelrepo()
    nc.apache()
    nc.php7()
    nc.nextcloud()
    nc.dbcreation()
    nc.selinux()
    nc.firewall()