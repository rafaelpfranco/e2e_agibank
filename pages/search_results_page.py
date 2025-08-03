# pages/results/search_results_page.py
from playwright.sync_api import Page, Locator
from config import settings

class SearchResultsPage:
    def __init__(self, page: Page):
        self._page: Page = page
        self._heading: Locator = page.locator(
            'h1.page-title.ast-archive-title:has-text("Resultados encontrados para:")'
        )
        self._term: Locator = self._heading.locator("span")
        self._articles: Locator = page.locator(
            "h2.entry-title.ast-blog-single-element a"
        )

    def get_heading(self) -> Locator:
        return self._heading

    def get_search_term(self) -> str:
        return self._term.inner_text().strip()

    def get_article_count(self) -> int:
        return self._articles.count()

    def get_article_link_by_index(self, index: int) -> Locator:
        return self._articles.nth(index)