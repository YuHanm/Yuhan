from Selenium.scr_baidu import Test
from selenium import webdriver
import unittest
class TestPoth(unittest.TestCase):
    def setUp(self):
        print('正在打开浏览器....')
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        print('浏览器已启动....')
    def test01(self):
        sp = Test(self.driver,self.url)
        sp.open(self.url)
        sp.get_scr()
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()