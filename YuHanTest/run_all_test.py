#coding = utf-8
import unittest
import time
import os
from YuHanTest.config import ReadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
try:
    from HTMLTestRunner.python2 import HTMLTestRunner
except:
        from HTMLTestRunner.python3 import HTMLTestRunner

def all_case():
    cur_path = './case/'
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(cur_path, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
    print(testcase)
    return testcase

def get_time():
    File_name = '%Y_%m_%d_%H_%M%S'
    return time.strftime(File_name, time.localtime(time.time()))

def get_daytime():
    Day = '%Y-%m-%d'
    return time.strftime(Day, time.localtime(time.time()))

def create_report(Daily_path):#报告路径
    filename = Daily_path + '/' + get_time() + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(all_case())
    fp.close()
    return Daily_path

def run():#判断存放报告的文件夹是否存在
    report_path = './Report_File/'
    Daily_path = report_path + get_daytime()
    if os.path.exists(Daily_path):
        create_report(Daily_path)
    else:
        os.mkdir(Daily_path)#使用os.mkdir创建文件夹
        create_report(Daily_path)
    return Daily_path #返回报告路径，发送邮件时通过os.listdir获取最新的报告路径

def get_report_file(Daily_path):
    '''获取最新的报告'''
    report_path = Daily_path
    # 利用os.listdir返回指定路径文件夹中的名字列表
    list = os.listdir(report_path)
    list.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print('最近一次的测试报告：  '+list[-1])
    report_file = os.path.join(report_path,list[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file, port):
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
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('测试报告已送达')

#执行用例
if __name__ == '__main__':

    sender = ReadConfig.sender
    psw = ReadConfig.psw
    smtp_server = ReadConfig.smtp_server
    port = ReadConfig.port
    receiver = ReadConfig.receiver
    # 加载执行用例，并将路径赋值给Daily_path
    Daily_path = run()
    # 获取报告路径
    report_file = get_report_file(Daily_path)
    # 发送报告
    send_mail(sender,psw,receiver,smtp_server, report_file,port)