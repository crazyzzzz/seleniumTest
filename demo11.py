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
        #self.driver.get('http://sahitest.com/demo/clicks.htm')

    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)
        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)

    def test_key(self):
        self.driver.get('https://www.baidu.com/')
        # kw = self.driver.find_element_by_id('kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL,'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL,'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL,'v')
        # sleep(2)

        element = self.driver.find_element_by_link_text('新闻')
        ActionChains(self.driver).move_to_element(element).click(element).perform()
        sleep(5)





if __name__ == '__main__':
    test = TestCase()
    #test.test_mouse()
    test.test_key()

