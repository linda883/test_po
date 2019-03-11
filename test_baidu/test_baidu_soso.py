from poium import Page, PageElement
from selenium import webdriver


class BaiduIndexPage(Page):
    search_input = PageElement(css='#kw')
    search_button = PageElement(css='#su')


driver = webdriver.Chrome(executable_path='/Users/liz/PycharmProjects/test_po/chromedriver')

page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input = "selenium"
page.search_button.click()

driver.quit()