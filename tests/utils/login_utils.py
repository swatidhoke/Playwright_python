from playwright.sync_api import Page
from .constants import ACCOUNT_URL ,LOGIN_URL, LOGIN_FORM_ERROR_SCREENSHOT

def login(page: Page, username: str, password: str):
    page.goto(LOGIN_URL)
    page.wait_for_timeout(5000)  # Wait 5 seconds for redirect/page load
    try:
        page.wait_for_selector('#username', timeout=20000)
    except Exception:
        page.screenshot(path=LOGIN_FORM_ERROR_SCREENSHOT)
        raise
    page.fill('#username', username)
    page.fill('input[type="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_timeout(5000)
     # Wait 10 seconds for potential redirects
    page.goto(ACCOUNT_URL)
   
    
