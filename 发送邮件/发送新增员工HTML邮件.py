from 邮件发送1 import send_mail#导入发送邮件模块
import smtplib
#smtp是一个邮件的传输协议它是来控制邮件发送的
from email.mime.text import  MIMEText
from email.header import Header
import os
# ff=r'D:\pythonProject\venv\7.13\.2021-07-13-12-47-11_result.html'
lists=os.listdir(r'D:/pythonProject/venv/7.13/')#文件路径
mail1=r"D:\pythonProject/venv/7.13/"+lists[-1]#拼接
print(mail1)
send_mail(mail1)