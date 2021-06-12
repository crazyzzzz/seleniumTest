from selenium import webdriver
import os
from time import sleep, strftime, localtime, time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        st=strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        file_name=st + '.png'
        self.driver.save_screenshot(file_name)






if __name__ == '__main__':
    test = TestCase()
    test.test1()

