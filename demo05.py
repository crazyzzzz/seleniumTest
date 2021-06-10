from selenium import webdriver
import os
from time import sleep
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms.html'
        print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        username=self.driver.find_element_by_id('username')
        username.send_keys('admin')
        pwd=self.driver.find_element_by_id('pwd')
        pwd.send_keys('123')
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))

        sleep(2)
        self.driver.find_element_by_id('submit').click()



if __name__ == '__main__':
    test = TestCase()
    test.test_login()
