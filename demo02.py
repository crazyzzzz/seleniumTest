from selenium import  webdriver
from time import sleep

class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        #print(type(element))

        self.driver.find_element_by_id('su').click()
        sleep(3)


    def test_name(self):
        #返回第一个元素
        element = self.driver.find_element_by_name('wd')
        #返回一个集合 self.driver.find_elements_by_name('wd')
        element.send_keys('selenium')
        #print(type(element))
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()
    
    def test_link_text(self):
        self.test_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)
        self.driver.quit()

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)
        self.driver.quit()

    def test_xpath(self):
        #返回第一个元素
        element = self.driver.find_element_by_xpath('//*[@id="kw"]')
        element.send_keys('selenium')
        #print(type(element))
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)
        self.driver.quit()

    def text_tag(self):
        input = self.driver.find_element_by_tag_name('input')
        print(input)

    def test_css_selector(self):
        #返回第一个元素
        element = self.driver.find_element_by_css_selector('#kw')
        element.send_keys('selenium')
        #print(type(element))
        self.driver.find_element_by_css_selector('#su').click()
        sleep(3)
        self.driver.quit()

    def test_class_name(self):
        # 返回第一个元素
        element = self.driver.find_element_by_class_name('s_ipt')
        element.send_keys('selenium')
        # print(type(element))
        self.driver.find_element_by_class_name('bg s_btn').click()
        sleep(3)
        self.driver.quit()

    def test_all(self):
        # 返回第一个元素
        element = self.driver.find_element(value='kw')
        element.send_keys('selenium')
        # print(type(element))
        self.driver.find_element_by_css_selector('#su').click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    testcase = TestCase()
    #testcase.test_id()
    #testcase.test_name()
    #testcase.test_link_text()
    #testcase.test_partial_link_text()
    #testcase.test_xpath()
    #testcase.text_tag()
    #testcase.test_css_selector()
    #testcase.test_class_name()
    testcase.test_all()

