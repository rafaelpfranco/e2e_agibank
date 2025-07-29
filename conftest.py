import pytest
from playwright.sync_api import sync_playwright
from config import settings

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(base_url=settings.BASE_URL)
        page = context.new_page()
        yield page
        browser.close()
