from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(1)
driver.find_element_by_id('kw').send_keys('suning')
sleep(1)
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()
