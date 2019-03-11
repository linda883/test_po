from poium import Page, PageElement


class BaiduIndexPage(Page):
    search_input = PageElement(css='#kw')
    search_button = PageElement(id_='su')