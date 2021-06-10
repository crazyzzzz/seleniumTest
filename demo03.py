from selenium import  webdriver
from time import  sleep

class  TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        self.driver.close() #只关闭当前tab

        #self.driver.quit()

    def test_method2(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)

if __name__ == '__main__':
    testCase = TestCase()
    #testCase.test_prop()
    #testCase.test_method()
    testCase.test_method2()

