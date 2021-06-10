from selenium import webdriver
import os
from time import sleep

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///"+path+"/forms3.html"
        print(file_path)
        self.driver.get(file_path)

    def test_select(self):
        se=self.driver.find_element_by_name('provise')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('bj')
        # sleep(2)
        # select.select_by_visible_text('Tianjing')
        # sleep(2)
        # self.driver.quit()

        for i in range(3):
            select.select_by_index(i)

        sleep(2)

        select.deselect_all()
        sleep(2)

        for option in select.options:
            print(option.text)

        self.driver.quit()





if __name__ == '__main__':
    test = TestCase()
    test.test_select()

