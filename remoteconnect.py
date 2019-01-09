import paramiko
import select
import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.0.12', port=22, username='root', password='Novi!234')
transport = client.get_transport()
channel = transport.open_session()
#print("Connection is available")
print (channel.exec_command("tail -f /var/log/auth.log")
#while True:
#rl, wl, xl = select.select([channel],[],[],0.0)
#if len(rl) > 0:
      #output = channel.recv(1024).decode("utf-8")
      #print (output)
      #fromaddr = "dikkalasrikanth4@gmail.com"
      #toaddr = "katturi.subhash@gmail.com"
      #msg = MIMEMultipart()
      #msg['From'] = fromaddr
      #msg['To'] = toaddr
      #msg['Subject'] = "log file alerts"
      #msg.attach(MIMEText(output))
     # server = smtplib.SMTP('smtp.gmail.com', 587)
      #server.starttls()
      #server.login(fromaddr, "Srikanth@1")
      #text = msg.as_string()
      #server.sendmail(fromaddr, toaddr, text)
