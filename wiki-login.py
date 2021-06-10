from selenium import webdriver
import os
from time import sleep
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('xxxxxxxxxxxxxxxxxxx')

    def test_login(self):
        username=self.driver.find_element_by_id('os_username')
        username.send_keys('xxxxx')
        pwd=self.driver.find_element_by_id('os_password')
        pwd.send_keys('xxxxxxxx')
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))

        sleep(2)
        self.driver.find_element_by_id('loginButton').click()



if __name__ == '__main__':
    test = TestCase()
    test.test_login()
