import yaml
import os
from Selenium.CSDN_Dome.Config.parameter import DATA_path
class RYaml():
    def get_yaml(self,file):
        scr_path = os.path.join(DATA_path,file)
        yml = yaml.load(open(scr_path,'rb'))
        return yml