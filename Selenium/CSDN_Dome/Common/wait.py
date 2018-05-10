import time

class Await:

    def Sleep(self,times):

        print('请等待%d秒...'%times)
        return time.sleep(times)

    def get_time(self,Day_name):

        return time.strftime(Day_name,time.localtime(time.time()))