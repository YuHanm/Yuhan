
import os

class  Test():
    def __init__(self,scdriver):
        self.driver = scdriver
    def get_scr(self):
        phont_path = '../png/'
        if not os.path.exists(phont_path):
            os.mkdir(phont_path)
        self.driver.get_screenshot_as_file(phont_path+'c.png')
