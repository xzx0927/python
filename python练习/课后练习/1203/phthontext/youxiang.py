import smtplib
from email.mime.text import MIMEText

host = 'smtp.163.com'
port = 465
sender = 'xiezixiang0927@163.com'
pwd = 'CTWEXGMAMURGRYLK'
# 连接服务器
con = smtplib.SMTP_SSL(host, port)
con.login(sender, pwd)
msg = MIMEText('123','plain','utf-8')
msg['Subject'] = '解子祥邮件'  # 主题
msg['From'] = sender
receivers = ['gouzhihong12138@163.com', 'lx394472@163.com','2747668191@qq.com']
msg['To'] = ','.join(receivers)
con.sendmail(sender, receivers, msg.as_string())
con.quit()
