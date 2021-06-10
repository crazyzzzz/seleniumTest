from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/test_alert.html"
        print(file_path)
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(2)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(2)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(2)
        prompt.send_keys('32')
        prompt.accept()
        print(prompt.text)




if __name__ == '__main__':
    test = TestCase()
    #test.test_alert()
    #test.test_confirm()
    test.test_prompt()

