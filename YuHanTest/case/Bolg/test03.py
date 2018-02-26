import unittest
import requests
import logging
logging.captureWarnings(True)
class Blog_login(unittest.TestCase):
    def login(self,username,psw,reme=True):
        url = 'https://passport.cnblogs.com/user/signin'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F',
            'VerificationToken': '7qnKaFqQcsoJJEanexnzq5U06qQV5AGr9iwCuzN81LDLHn4KiajfgIS-YwLtq0PH4jgiaTX1Fa8W98GTAzA2lgYUBbk1:V_Ee2cy1EURwwVJgQkM1f9xiPwMXSnzQAo_HuHb0QGa82j81_jGRyvgNqy57ug7jDyT2TCdhln9gJ03eHXxb-L6RgaY1',
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '385',
            'Cookie': '__gads=ID=8f4d905077710513:T=1502684750:S=ALNI_MZGaRGHneFWoxMbup5QMTe_4OTVFg; UM_distinctid=15df337cf6b9a8-0829a122fbafd9-8383667-1fa400-15df337cf6c49c; _ga=GA1.2.1674668413.1502678266; _gid=GA1.2.2115056122.1507864240; _gat=1; SERVERID=dcc5cb8c464da84cc9928c22dd5884f8|1507878534|1507878532',
            'Connection': 'keep-alive'
        }
        json_data = {
            'input1': username,
            'input2':psw,
            'remember':reme
        }
        res = requests.post(url,headers = head,json = json_data,verify = False)
        result1 = res.content
        print(result1)
        return res.json()
    def test_login1(self):
        username = 'WPwvVmLlpwYrNaBRkWnMbd7FAA9BQ675YqcM3QgtvdTm5bc9cFZSZH16qk6um92/s80ShhSfGLYnYIDNx1MpIufomQzoiKjWGlxtEW0gDH4lBu1Yf3ue05lDkUaPnpo7pZpH6wYFLQbjuzTWUh+N+zSaTK3FIc6At+NZejUrPn4='
        psw = 'n1YIBTDLybMzzgvi408KrMydGWBWRhBOlIs16nW9p6OaOhZPQMLNhgATJVCohH1GrfKuoqCOtMbbkt8XAwSKLC6EjXPg46e2PdR3QxXJT7Jd7gIoOuSN2yaqb9922LTe1eu2zEu9NqtWBPNbJ0l2WV0oECGprQZOibhSnetwWYA='
        result = self.login(username,psw)
        self.assertEqual(result['success'],True)
    def test_login2(self):
        username = 'tXSXHMMEpnR2zWuDDhi0JuM/IKmC1LPlIFkPLCxDN5mlxuzBwhYCyCrIkoeRjvsdlQW5aww18fIYQU6bK2HqehqYt5G/qvohONEMZmr7OcG4+I+R/W0wfE8YJXI8ZGJmXTsw/E76rcoAHt3+RR/EkklG35+JJHECjw+kKM0JYg=',
        psw = 'WcfhHVmg8ncrkaZNttm1Vf2XIxx6KLQXaOK6L+MCjkrMA9XBW0X6zufqjqeKIxJKLyIN9s6GgzLd5TlhInlbvQErCFTud6rVnUNRsJQQoVPs8Y3wmAPLibgpod9yi5Gk7JjJZtx1q9bmcsUiZ+2NClt4+B/LbljGTPxhVF7bto=',
        result = self.login(username,psw)
        self.assertEqual(result['success'],False)