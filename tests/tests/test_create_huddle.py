import pytest
from playwright.sync_api import sync_playwright
from tests.utils.constants import USERNAME, PASSWORD, ACCOUNT_URL
from tests.utils.login_utils import login
from tests.utils.test_data import huddles

@pytest.mark.parametrize("huddle_data", huddles) 
def test_create_multiple_huddles(huddle_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        login(page, USERNAME, PASSWORD)
        page.wait_for_url(ACCOUNT_URL, timeout=25000)
        assert page.url == ACCOUNT_URL
        page.wait_for_timeout(3000)

        # Handle initial popups
        okay_button = page.get_by_role("button", name="Okay")
        if okay_button.is_visible():    
            okay_button.click()  
            page.wait_for_timeout(2000)

        for huddle_data in huddles:
            # Open Huddle creation dialog
            page.click('button#plus')
            page.locator("#plus_huddle").click()
            page.wait_for_timeout(1000)

            # Handle popups again
            okay_button = page.get_by_role("button", name="Okay")
            if okay_button.is_visible():    
                okay_button.click()     
                page.wait_for_timeout(500)

            # Fill Huddle details
            page.fill("#eventName", huddle_data["eventName"])

            # Quill editor for description
            quill_editor = "div.ql-editor.ql-blank"
            page.click(quill_editor)
            page.fill(quill_editor, huddle_data["description"])
            page.wait_for_timeout(1000)

            # Submit form
            page.locator("#save").click()
            page.wait_for_timeout(10000)  # Wait for creation to finish

        browser.close()
