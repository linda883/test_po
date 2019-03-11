from poium import Page, PageElement
from poium.page_objects import PageWait
from selenium import webdriver
import unittest
from pageobject.page.BaiduFirstPage import BaiduIndexPage
from pageobject.page.SouResultPage import SoResultPage
from time import sleep

class TestBaiduSo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/liz/PycharmProjects/test_po/chromedriver')

    def test_soso(self):
        page = BaiduIndexPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()
        page_result = SoResultPage(self.driver)
        sleep(2)
        # PageWait(page_result.search_result_text)
        assert "selenium" in page_result.get_title

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()