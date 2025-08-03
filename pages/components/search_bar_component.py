from playwright.sync_api import Page, Locator
from config import settings

class SearchBarComponent:
    def __init__(self, page: Page):
        self._page = page
        self._input_search: Locator = page.get_by_role("searchbox", name="Pesquisar por:")
        self._button_search: Locator = page.get_by_role("button", name="Search button")

    def search(self, term: str) -> None:
        self._button_search.wait_for(state="visible", timeout=settings.TIMEOUT)
        self._button_search.click()

        self._input_search.wait_for(state="visible", timeout=settings.TIMEOUT)
        self._input_search.fill(term)
        self._input_search.press('Enter')
