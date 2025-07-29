from playwright.sync_api import Page
from pages.components.newsletter_component import NewsletterComponent

class NewsPage:
    def __init__(self, page: Page):
        self._page = page
        self._url_path = "/noticias/"
        self._newsletter = NewsletterComponent(page)

    @property
    def newsletter(self) -> NewsletterComponent:
        return self._newsletter

    def navigate(self) -> None:
        self._page.goto(self._url_path)
