import os
import pytest
from playwright.sync_api import sync_playwright
from config import settings

@pytest.fixture(scope="function")
def page():
    browser_name = os.getenv("BROWSER", "chromium")
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        context = browser.new_context(base_url=settings.BASE_URL)
        page = context.new_page()
        yield page
        browser.close()
