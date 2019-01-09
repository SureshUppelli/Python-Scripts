
# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("suresh.uppapalli@gmail.com", "suresh@9666")

# message to be sent
message = "Hi this is test mail from python code"

# sending the mail
s.sendmail("suresh.uppapalli@gmail.com", "ajaygunna206@gmail.com", message)

# terminating the session
s.quit()
