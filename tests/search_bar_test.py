# tests/search_results_test.py
import pytest
from pages.home_page import HomePage
from pages.components.search_bar_component import SearchBarComponent
from pages.search_results_page import SearchResultsPage
from playwright.sync_api import expect
from fixtures.search_terms import SearchTerms
from config import settings

@pytest.mark.usefixtures("page")
class TestSearchFlow:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.home = HomePage(page)
        self.home.navigate()
        self.home.get_carousel().wait_for(state="visible", timeout=settings.TIMEOUT)
        self.search_bar = SearchBarComponent(page)
        

    def test_search_and_validate_results(self):
        """
        Verifica que uma busca por termo existente retorna resultados.
        """
        term = SearchTerms.EXISTING_TERM
        self.search_bar.search(term)

        expect(self.page).to_have_url(
            "/?s=" + term,
            timeout=settings.TIMEOUT
        )

        results = SearchResultsPage(self.page)

        results.get_heading().wait_for(state="visible", timeout=settings.TIMEOUT)
        assert "Resultados encontrados para:" in results.get_heading().inner_text()
        assert results.get_search_term() == term

        count = results.get_article_count()
        assert count > 0

        for idx in range(count):
            card = results.get_article_link_by_index(idx)
            assert card.is_visible()

    def test_search_with_no_results(self):
        """
        Verifica que uma busca por termo inexistente não retorna resultados.
        """
        term = SearchTerms.NO_RESULTS_TERM
        self.search_bar.search(term)

        expect(self.page).to_have_url(
            "/?s=" + term,
            timeout=settings.TIMEOUT
        )

        results = SearchResultsPage(self.page)
        results.get_heading().wait_for(state="visible", timeout=settings.TIMEOUT)
        assert "Resultados encontrados para:" in results.get_heading().inner_text()
        assert results.get_search_term() == term

        count = results.get_article_count()
        assert count == 0