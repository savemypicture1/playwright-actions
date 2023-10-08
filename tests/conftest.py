import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def actions_driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        yield page
        context.close()
        browser.close()
