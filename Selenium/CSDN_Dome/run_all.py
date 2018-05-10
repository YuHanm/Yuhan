import unittest
import os
try:
    from TestRunner.python2 import HTMLTestRunner
except:
    from TestRunner.python3 import HTMLTestRunner
from Selenium.CSDN_Dome.Email.mail import Mail
from Selenium.CSDN_Dome.Config import parameter

#构建测试套件

def all_case():
    Case_path = os.path.join(os.getcwd(),'Case')
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(Case_path, pattern='test*.py', top_level_dir=None)
    #print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)

    return testcase

def create_report():#报告路径
    filename = parameter.Report_path +'/'+'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(all_case())
    fp.close()
    return filename


if __name__ == '__main__':

    Report = create_report()

    sender = parameter.sender
    psw =parameter.psw
    smtp_server = parameter.smtp_server

    report_file = Report
    port = parameter.port
    receiver = parameter.receiver
    fs =Mail()
   # fs.send_mail(sender, psw,receiver, smtp_server,report_file, port)