import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from tests.utils.constants import USERNAME, PASSWORD, ACCOUNT_URL
from tests.utils.login_utils import login

def test_login_missionpeak():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            login(page, USERNAME, PASSWORD)
        finally:
            context.close()
            browser.close()