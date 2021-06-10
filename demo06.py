from selenium import webdriver
import os
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/forms2.html"
        print(file_path)
        self.driver.get(file_path)

    def test_checkbox(self):
        swimming=self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        reading=self.driver.find_element_by_name('reading')
        if not reading.is_selected():
            reading.click()
        sleep(5)
        swimming.click()
        sleep(3)

    def test_radio(self):
        genders = self.driver.find_elements_by_name('gender')
        genders[1].click()
        sleep(5)

        if genders[1].is_selected():
            genders[0].click()

if __name__ == '__main__':
    test = TestCase()
    #test.test_checkbox()
    test.test_radio()


