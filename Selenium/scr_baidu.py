import os

class  Test(object):
    #初始化浏览器，URL地址
    def __init__(self,sc_driver,sc_url):
        self.driver = sc_driver
        self.sc_url = sc_url
    #打开连接
    def open(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('网站未正确打开...%s'%url)
    #截图
    def get_scr(self):
        try:
            phont_path = '../png/'
            if not os.path.exists(phont_path):os.mkdir(phont_path)
            return self.driver.get_screenshot_as_file(phont_path+'c.png')
        except Exception as e:
            print('图片未保存成功...')
