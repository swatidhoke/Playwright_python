import pytest
from playwright.sync_api import sync_playwright
from tests.utils.constants import USERNAME, PASSWORD, ACCOUNT_URL
from tests.utils.login_utils import login

def test_launch_missionpeak():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://missionpeak.app/account")
        assert 'Mission Peak' in page.title()
        browser.close()
