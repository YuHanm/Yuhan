import os
from configparser import ConfigParser
from Selenium.CSDN_Dome.Common.wait import Await
'''
配置全局参数
'''

#获取项目的路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.relpath(__file__)[0]),'.'))

#获取截图路径，并判断路径是否存在
img_path =  './Img/'
if not os.path.exists(img_path):os.mkdir(img_path)

#报告文件夹
s=Await()
t = '%Y-%m-%d'
Report = os.path.join(os.getcwd(),'Report')
Report_path = Report +'/'+s.get_time(t)

if not os.path.exists(Report):os.mkdir(Report)

if not os.path.exists(Report_path):os.mkdir(Report_path)



#加载邮箱配置
DATA_path = os.path.join(os.getcwd(),'Data')

configPath = os.path.join(DATA_path, "email.ini")

conf = ConfigParser()

conf.read(configPath)

smtp_server = conf.get("email", "smtp_server")

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")

#Yaml文件
Ypath = os.path.join(DATA_path,'Element')
