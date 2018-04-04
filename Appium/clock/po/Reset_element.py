class Reset():
    #初始化连接
    def __init__(self,se_driver):
        self.driver = se_driver

    def find_element(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print('%s未找到'%(self,loc))