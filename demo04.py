from selenium import  webdriver
from time import  sleep

#http://sahitest.com/demo/
class  TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.driver.maximize_window()
        sleep(1)

    def test_webelement_prop(self):
        e= self.driver.find_element_by_id('t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect) #宽高和坐标
        print(e.text)

    def test_webelement_method(self):
        e= self.driver.find_element_by_id('t1')
        e.send_keys('hello World')
        sleep(2)


        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()

    def test_webelement_method2(self):
        e= self.driver.find_element_by_id('t1')
        e.send_keys('hello World')
        sleep(2)
        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()





if __name__ == '__main__':
    testCase = TestCase()
    testCase.test_webelement_method()

