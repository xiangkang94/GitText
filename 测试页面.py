#coding:utf-8
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
import requests
driver = selenium.webdriver.Chrome()
driver.get("https://passport.csdn.net/account/login?")
time.sleep(3)


user=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
submit=driver.find_element_by_class_name("logging")
user.clear()
password.clear()
time.sleep(1)
user.send_keys("yincheng01@163.com")
password.send_keys("yinchengak47.net")
time.sleep(1)
submit.click()
time.sleep(10) #等待页面加载，
cookies=driver.get_cookies()#抓取全部的cookie
driver.close()

print ("开始会话")
req=requests.session()#会话

for  cookie  in cookies:
    req.cookies.set(cookie['name'],cookie["value"])
req.headers.clear()#清空头
newpage=req.get("http://my.csdn.net/")
print ("会话完成")
print (newpage.text)  #页面
time.sleep(10)