from selenium import webdriver
import time
import os
#'--user-data-dir=C:\Users\Avazu Holding\AppData\Local\Google\Chrome\User Data\Profile 4\Default'

driver =webdriver.Chrome()
driver.maximize_window()
cur_path=os.path.join(os.getcwd(),'frame.html')
url ='file:///'+cur_path

driver.get(url)
#勾选单个复选框
#driver.find_element_by_id('c1').click()
driver.find_element_by_id('boy').click()

r=driver.find_element_by_id('boy').is_enabled()
print(r)
#勾选多个
checkboxs=driver.find_elements_by_xpath('.//*[@type="checkbox"]')
for o in checkboxs:
    time.sleep(3)
    o.click()
time.sleep(10)
#操作表单
t = driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[2]/td[1]')
print(t.text)
driver.quit()