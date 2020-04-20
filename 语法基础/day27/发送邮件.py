"""
发送邮件
@Date 2020.04.20
smtplib和email为python内置模板
"""
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
# 负责构造邮件头信息
from email.header import Header
# SMTP服务器，这里使用qq邮箱
mail_host = "smtp.qq.com"
# 发件人邮箱
mail_sender = "1244353765@qq.com"
# 邮箱授权码，注意这里不是邮箱密码！！！
mail_license = "gjripthykmtrghfg"
# 收件人邮箱，可以为多个收件人
mail_receivers = ["16422802@qq.com"]
# 构建
mm = MIMEMultipart('related')
# 邮件主题
subject_content = """Python邮件测试"""
# 设置发送者，注意格式，里面邮箱为发件人邮箱
mm["From"] = "王锋<1244353765@qq.com>"
mm["To"] = "陶然然<16422802@qq.com>"
# 设置主题
mm["Subject"] = Header(subject_content, 'utf-8')
# 邮件正文内容
body_content = """hello, 这是蜂王发的邮件-- happy every day!!!"""
message_text = MIMEText(body_content, "plain", "utf-8")
mm.attach(message_text)
atta = MIMEText(open('./语法基础/res/excel/demo.xlsx', 'rb').read(), 'base64', 'utf-8')
atta["Content-Disposition"] = 'attachment; filename="excel_demo2.xlsx"'
mm.attach(atta)
stp = smtplib.SMTP()
stp.connect(mail_host, 25)
stp.set_debuglevel(1)
stp.login(mail_sender, mail_license)
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
stp.quit()