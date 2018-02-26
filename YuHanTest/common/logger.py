#coding = utf-8
import logging,time,os
#本地日志文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'Logs')
if not os.path.exists(log_path):os.mkdir(log_path)

class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输入出格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-%(levelname)s:%(message)s')
    def __consle(self,level,message):
        # 创建一个fileHandler,用于把日志写到本地
        #fh = logging.FileHandler(self.logname,'a')#这个是Python2版本的写法
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')#这个是Python3版本的写法
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个SteamHandler，用于输出到控制台

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self.__consle('debug',message)

    def info(self,message):
        self.__consle('info',message)

    def warning(self,message):
        self.__consle('warning',message)

    def error(self,message):
        self.__consle('error',message )

