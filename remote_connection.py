import paramiko

ip='192.168.3.87'
port=22
username='sharmila'
password='Novi1234'

cmd='df -hT'

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

#stdin,stdout,stderr=ssh.exec_command('some really useful command')
#outlines=stdout.readlines()
#resp=''.join(outlines)
#print(resp)
