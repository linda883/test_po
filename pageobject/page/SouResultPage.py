from poium import Page, PageElement


class SoResultPage(Page):
    search_result_text = PageElement(css='#s_tab > div > b', timeout=2)

