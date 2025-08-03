from playwright.sync_api import Page, Locator
from config import settings

class HomePage:
    def __init__(self, page: Page):
        self._page: Page = page
        self._carousel: Locator = page.locator(
            'div.wp-block-uagb-post-carousel.is-carousel'
        )
        self._search_bar_button: Locator = page.get_by_role("button", name="Buscar")

    def navigate(self):
        self._page.goto(settings.BASE_URL)

    def get_carousel(self) -> Locator:
        return self._carousel

    def get_search_button(self) -> Locator:
        return self._search_bar_button