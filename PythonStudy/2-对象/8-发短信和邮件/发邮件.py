

# 发邮件的库
import smtplib

# 邮件文本
from email.mime.text import MIMEText


# 需要一个服务器
SMTPServer = 'smtp.163.com'

# 发邮件地址
sender = 'quanjunt0929@163.com'

# 发送者邮箱密码(授权密码, 非邮箱登录密码)
passwd = 'jun0929'


# 设置发送的内容
message = 'https://www.titanjun.top/'

# 转成邮件文本格式
msg = MIMEText(message)

# 标题
msg['Subject'] = "Titanjun"

# 发送者
msg['From'] = sender


# 创建SMTP服务器, 25端口号
mailServer = smtplib.SMTP(SMTPServer, 25)

# 登录邮箱
mailServer.login(sender, passwd)

# 发送邮件
# 收件人
list = ["quanjunt@163.com"]
print(msg.as_string())
mailServer.sendmail(sender, list, msg.as_string())

# 退出邮箱
mailServer.quit()

