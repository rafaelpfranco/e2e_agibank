# conftest.py
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
            args=[
                "--lang=pt-BR",
                "--disable-gpu",
                "--enable-features=NetworkService",
                "--disable-dev-shm-usage"
            ]
        )
        context = browser.new_context(
            base_url=settings.BASE_URL,
            locale="pt-BR",
            viewport={"width": 1280, "height": 720},
            device_scale_factor=1
        )
        context.route("**/*.{png,jpg,jpeg,svg,gif,css,woff2,ttf}", lambda route: route.abort())
        page = context.new_page()
        page.set_default_timeout(settings.TIMEOUT * 2)
        page.goto(settings.BASE_URL, wait_until="networkidle")
        yield page
        browser.close()
