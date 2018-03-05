#coding = utf-8
import unittest
import requests
from common.logger import Log
from case.CSDN import login_csdn

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        s = requests.session()
        self.csdn = login_csdn.CSDN(s)

    def login(self):

        self.log.info('----测试开始----')
        result = self.csdn.test_login()
        self.log.info('调用登录结果：%s'%result)
        self.log.info('获取是否登录成功：%s'%result['success'])
        self.log.info(result['success'],True)
        self.log.info('----end-----')
