# coding = utf-8
import requests
from bs4 import BeautifulSoup
import lxml
import unittest
import re
import logging

logging.captureWarnings(True)

class CSDN():
    #设置接口访问头部
    def __init__(self,url):
        self.url = url
        self.heard = {
            # 'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            # #'Content-Length': '121',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Referer': 'https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn',
            # 'Connection': 'keep-alive',
            # #'Host': 'passport.csdn.net',
            # #'Origin': 'https://passport.csdn.net',
            # 'Upgrade-Insecure-Requests': '1',
            # 'Cookie': 'uuid_tt_dd=-7728607757242185364_20170817; UM_distinctid=15e65c091fe44f-0ee8a5c6fee38e-8383667-1fa400-15e65c091ffc1d; UN=qq_26828953; UE="1138941694@qq.com"; BT=1508918774960; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1508830000,1508905724,1508915790,1508920088; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1508920159; dc_tos=oyde8u; dc_session_id=1508920088880_0.13812351458559347'
        }
        self.s = requests.session()
    #登录CSDN

    def test_login(self):
        #先获取登录流水号
        r = self.s.get(self.url,headers=self.heard,verify=False)
        html = r.text
        print(html)
        sop = BeautifulSoup(html, 'lxml')
        # sop = BeautifulSoup(html,'html.parser')
        #通过BeautifulSoup的find_all方法查询出lt...的值，再通过正则提取
        All_input = sop.find_all('input', {'name': {'lt', 'execution','_eventId'}})
        value = re.findall('value="(.*?)"', str(All_input))
       # print(All_input)
       #  lt_value = sop.find('input', {'name': 'lt'})['value']
        # execution_value = sop.find('input', {'name': 'execution'})['value']
      #  print(lt)
        lt_value = value[0]
        execution_value = value[1]
      #   submit_value = value[2]

        data = {
           # 'from': 'http://my.csdn.net/my/mycsdn',
            'username': '1138941694@qq.com',
            'password': '521125',
            'lt': lt_value,
            'execution': execution_value,
            '_eventId': 'submit'
        }
        r2 = self.s.post(self.url, headers=self.heard, data=data, verify=False)
        #print(r2.text)
    def get_csdn(self):
        url1 = 'http://my.csdn.net/my/mycsdn'
        r3 = self.s.get(url1, headers=self.heard,verify=False)
        print(r3.text)
if __name__ == '__main__':
    url ='https://passport.csdn.net/account/login;jsessionid=E3EAD22D686CC6FDF89AC7615F4E42B4.tomcat2?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn'
    app =CSDN(url)
    app.test_login()
    app.get_csdn()