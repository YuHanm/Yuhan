import time
import re
import requests
import platform
print(platform.python_version())
# tmp = int(time.time())
# print(tmp)
# t=time.time()
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#获取时间戳，精确到毫秒3位数
# print (time.strftime('%Y-%m-%d %H:%M:%S') + ':' + re.sub('^0\.','',str((round((t-int(t)),3)))))
url = 'https://passport.csdn.net/account/login;jsessionid=2538A72244210897EE9C0638779B0BB7.tomcat1?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'
s = requests.session()
print(s)
