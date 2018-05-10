from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://passport.csdn.net/account/login')
print("-------开始登陆-------")
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
time.sleep(5)
driver.find_element_by_css_selector('#username').send_keys('1138941694@qq.com')
time.sleep(5)
driver.find_element_by_css_selector('.pass-word').send_keys('Gzq0908..')
driver.find_element_by_class_name('logging').click()
time.sleep(5)
#鼠标悬停
blogs = driver.find_element_by_css_selector('.loginCenter')
ActionChains(driver).move_to_element(blogs).perform()
time.sleep(4)
#获取当前窗口句柄
print(driver.title)
#点击博客
driver.find_element_by_css_selector('.toolbar_to_feed').click()

#切换窗口

time.sleep(10)
all_h = driver.window_handles
print(all_h)
driver.switch_to.window(all_h[0])
print(driver.title)
print("------登陆成功-----")