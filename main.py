from unittest import TestCase
from selenium import webdriver


class SearchText(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\nathan\\chrome_driver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        test_file = 'C:\\Users\\nathan\\repos\\selenium_testing\\testing.html'
        self.driver.get(test_file)

    def test_search_by_id(self):
        self.list_item = self.driver.find_element_by_id('first')

        print(self.list_item.text)
        self.assertEqual(self.list_item.text, 'Nathy')
