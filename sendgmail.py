import smtplib

host = "smtp.gmail.com"
port = 587
username = "suresh.uppelli123@gmail.com"
password = "Novi1234"
from_email = "suresh.uppelli123@gmail.com"
to_list = ["suresh.uppelli123@gmail.com", "suresh.uppapalli@gmail.com"]
email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello this is Testing Message from python")
email_conn.quit()
