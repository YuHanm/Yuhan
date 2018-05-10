from Selenium.CSDN_Dome.Config.parameter import img_path
from ..Common import logger
'''
webdriver基类构建
'''
class Method(object):

    #初始化浏览器
    def __init__(self,sr_driver,sr_url):

        self.driver = sr_driver
        self.url = sr_url
        self.mylog = logger.Log()

    #打开页面
    def _open(self,url):
        try:
            self.driver.get(url)
            self.mylog.info('页面正常打开:'+url)
        except:
            self.mylog.error('未打开正确到页面:'+url)

    # 页面元素操作封装
    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except:
            self.mylog.error('未找到元素:' + str(loc))

    # 重写send_keys输入方法
    def send_keys(self, value, clear=True, *loc):
         try:
             self.mylog.info('正在输入信息:' + str(loc) + value)
             if clear:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(value)
         except AttributeError:
             self.mylog.error('输入失败:' + str(loc) + value)

    #浏览器最大化
    def MaxWindow(self):
        self.driver.maxmize_window()

    #判断浏览器title
    def JTitle(self,sr_title):
        try:
            self.driver.title(sr_title)
        except :
            print('%s页面异常'%(sr_title))

    #截图方法
    def img_screenshot(self,img_name):
        try:
            return self.driver.get_screenshot_as_file(img_path + img_name + '.png')
        except :
            self.mylog.error('截图失败：'+img_name)

