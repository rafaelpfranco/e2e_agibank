import os
import pytest
from playwright.sync_api import sync_playwright
from config import settings

@pytest.fixture(scope="function")
def page():
    browser_name = os.getenv("BROWSER", "chromium")
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(
            headless=True,
            channel="chrome",
            args=["--lang=pt-BR"]
        )
        context = browser.new_context(
            base_url=settings.BASE_URL,
            locale="pt-BR",
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()
        try:
            yield page
        finally:
            context.tracing.stop(path="trace.zip")
            browser.close()
