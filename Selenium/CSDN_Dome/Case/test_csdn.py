import unittest

from selenium import webdriver

from Selenium.CSDN_Dome.Page.login_page import log_in


'''
CSDN PO 模式分层学习Dome
'''

class TestCSND(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''打开CSDN登陆页面'''
        cls.driver = webdriver.Chrome()
        cls.url = 'https://passport.csdn.net/account/login'
        cls.login = log_in(cls.driver,cls.url)
        cls.user = '1138941694@qq.com'
        cls.psw = 'Gzq0908..'

    def test_login01(self):
        try:
            self.login.open()
        except Exception as e:
            self.login.img_screenshot('登陆页面异常')
            raise e
    def test_login02(self):
        try:
            self.login.click_way()
            self.login.iput_msg(self.user,self.psw)
        except Exception as e:
            self.login.img_screenshot('账号密码输入异常')
            raise e
        try:
            self.login.loging()
            self.login.img_screenshot('登陆成功')
        except Exception as e:
            self.login.img_screenshot('登陆失败')
            return e
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()