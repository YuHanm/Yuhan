# coding:utf-8
import os
from configparser import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cof.ini")
conf = ConfigParser()
conf.read(configPath)

smtp_server = conf.get("email", "smtp_server")

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")