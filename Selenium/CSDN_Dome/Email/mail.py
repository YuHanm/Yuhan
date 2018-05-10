from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..Common.logger import Log
import smtplib
import os

class Mail:

    def __init__(self):
        self.mylog = Log()

    def send_mail(self,sender, psw, receiver, smtpserver, report_file, port):
        '''发送最新的测试报告内容'''
        with open(report_file, "rb") as f:
            mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = "自动化测试报告"
        msg["from"] = sender
        msg["to"] = psw
        msg.attach(body)
        # 添加附件
        att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)
        try:
            #判断邮箱通讯协议
            if  smtplib.SMTP_SSL:
                smtp = smtplib.SMTP_SSL(smtpserver, port)
            else:
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver, port)
        # 用户名密码
            smtp.login(sender, psw)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            self.mylog.info('测试报告已送达')
        except smtplib.SMTPException:
            self.mylog.error('邮件发送失败')

    # 获取最近的报告发送
    # def get_report(self,Report):
    #     report = Report
    #     list = os.listdir(report)
    #     list.sort(key=lambda fn: os.path.getmtime(os.path.join(report, fn)))
    #     print('最近一次的测试报告：  ' + list[-1])
    #     report_file = os.path.join(report, list[-1])
    #     return report_file

