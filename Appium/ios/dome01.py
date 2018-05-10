from appium import webdriver

cap ={
    'platformName':'ios',
    'platformVersion':'11.3',
    'deviceName':'iPhone 7',
    'browserName':'safari'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',cap)
driver.get('https://www.baidu.com')