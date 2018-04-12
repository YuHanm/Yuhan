from selenium import webdriver
import time
class Method(object):

#初始化浏览器
    def __init__(self,sr_driver):
        try:
            self.driver = sr_driver
        except:
            print('%s浏览器没有找到'%(sr_driver))

#浏览器最大化
    def MaxWindow(self):
