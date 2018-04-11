from appium import webdriver
from clock.po.operate import CreatPage
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        caps ={
          "platformName": "Android",
          "deviceName": "M3LDU15902004692",
          "platformVersion": "4.4.2",
          "appPackage": "mobi.clock.android",
          "appActivity": "com.philliphsu.clock2.startup.StartupPageActivity"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
#点击创建闹钟
    def test_clock(self):
        sp = CreatPage(self.driver)
        sp.run_case()
if __name__ =='__main__':
    unittest.main()
#driver.find_element_by_id('com.philliphsu.clock2.debug:id/fab').click()
#
# driver.find_element_by_id('com.philliphsu.clock2.debug:id/action_settings').click()
# #driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Settings"]').click()