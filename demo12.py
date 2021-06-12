from selenium import webdriver
import os
from time import sleep

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
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js='return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        js ='var q = document.getElementById("kw");q.style.border="2px solid red"'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js ='window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)





if __name__ == '__main__':
    test = TestCase()
    #test.test1()
    test.test4()

