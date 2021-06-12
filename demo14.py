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
        self.driver.get('http://sahitest.com/demo/framesTest.htm')

    def test1(self):
        top = self.driver.find_element_by_name('top')
        self.driver.switch_to.frame(top)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(2)
        self.driver.switch_to.default_content()
        second = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(5)
        self.driver.quit()






if __name__ == '__main__':
    test = TestCase()
    test.test1()

