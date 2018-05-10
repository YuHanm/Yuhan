from Selenium.CSDN_Dome.Method.method import Method
from selenium.webdriver.common.by import By
from Selenium.CSDN_Dome.Common.wait import Await
from Selenium.CSDN_Dome.Common.redYaml import RYaml
from Selenium.CSDN_Dome.Config.parameter import Ypath
class log_in(Method):
    yml=RYaml().get_yaml(Ypath)
    ueser_name = (By.CSS_SELECTOR,yml['login']['账号'])
    pasword = (By.CSS_SELECTOR,yml['login']['密码'])
    login_name = (By.CLASS_NAME,yml['login']['登陆按钮'])
    login_way = (By.XPATH,yml['login']['切换'])


    time = Await()
    #打开页面
    def open(self):
        self._open(self.url)

    #切换到账号登陆
    def click_way(self):

        self.find_element(*self.login_way).click()
        self.time.Sleep(5)

    #输入账号密码
    def iput_msg(self,user,psw):
        self.find_element(*self.ueser_name).send_keys(user)
        self.time.Sleep(3)
        self.find_element(*self.pasword).send_keys(psw)
        self.time.get_time('%Y-%m-%d')
        self.time.Sleep(5)

    #点击登陆
    def loging(self):
        self.find_element(*self.login_name).click()
        home = self.driver.title
        self.mylog.info('登陆后首页：%s'%home)
        self.time.Sleep(5)