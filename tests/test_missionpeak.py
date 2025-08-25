import pytest
from playwright.sync_api import sync_playwright

def test_launch_missionpeak():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://missionpeak.app/start")
        assert 'Mission Peak' in page.title()
        browser.close()
