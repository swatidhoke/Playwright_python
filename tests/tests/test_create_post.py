import code
import time
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from tests.utils.constants import USERNAME, PASSWORD, ACCOUNT_URL
from tests.utils.login_utils import login
from tests.utils.test_data import posts 
from concurrent.futures import wait
import pytest
from playwright.sync_api import sync_playwright 


@pytest.mark.parametrize("post_data", posts)
def test_create_multiple_posts(post_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="test-results/videos")
        page = context.new_page()
        try:
            login(page, USERNAME, PASSWORD)
            page.wait_for_url(ACCOUNT_URL, timeout=25000)
            assert page.url == ACCOUNT_URL
            # Navigate to post creation
            page.click('button#plus')
            page.click('li#plus_post')
            # Set post text using evaluate for Quill editor
            quill_editor = "div.ql-editor"
            post_text = post_data["text"]
            page.wait_for_selector(quill_editor, timeout=15000)
            page.click(quill_editor)
            page.type(quill_editor, post_text)
            time.sleep(0.5)
            #Location 
            try:
                page.locator('span.material-icons.cursor-pointer', has_text="location_on").first.click()
                print("Location icon clicked")
                page.wait_for_selector('input[placeholder="Enter Location"]', timeout=10000)
            except Exception as e:
                print(f"Location icon or input not found: {e}")
                raise
            try:
                time.sleep(0.5)
                page.fill('input[placeholder="Enter Location"]', post_data.get("location", ""))
                time.sleep(0.5)
                page.locator(".pac-item").first.click()
                time.sleep(0.5)
                page.get_by_role("button", name="Select Location").click()
                time.sleep(0.5)
            except Exception as e:
                print(f"Location fill failed: {e}")
                raise
            page.wait_for_timeout(1000)
           ##Create Post
            try:
                page.click('button#createPost')
                print("Create post button clicked")
                time.sleep(0.5)
                page.wait_for_selector('text=Post created successfully', timeout=10000)
                print("Post creation verified")
            except Exception as e:
                print(f"Post creation failed: {e}")
                raise
        finally:
            page.close()
            context.close()
            browser.close()

def test_single_post_creation() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login(page, USERNAME, PASSWORD)
        page.wait_for_url(ACCOUNT_URL, timeout=25000)
        assert page.url == ACCOUNT_URL

        # Add post
        page.get_by_role("button", name="add", exact=True).click()
        page.locator("a", has_text="Post Broadcast something").click()
        editor = page.locator("p-editor div").nth(3)
        editor.click()
        editor.fill("my playwright create post test")
        # Post
        page.get_by_role("button", name="Post").click()
        page.get_by_text("View Post").click()

def test_single_post_creation_withTags() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to login page
        page.goto("https://missionpeak.app/account")
        # Login
        page.get_by_label("Email address").fill("swatidhoke@gmail.com")
        page.get_by_label("Password").fill("missionPeak1!")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Okay").click()

        # Add post
        page.get_by_role("button", name="add", exact=True).click()
        page.locator("a", has_text="Post Broadcast something").click()
        editor = page.locator("p-editor div").nth(3)
        editor.click()
        editor.fill("my playwright create post test")

        # Select user
        page.get_by_text("person_add").click()
        page.locator("app-user-picker-new").get_by_role("button").click()
        page.get_by_role("button", name="Select User").click()
        page.wait_for_timeout(10000)

        # Post
        page.get_by_role("button", name="Post").click()
        page.get_by_text("View Post").click()

def test_single_post_creation_withLocation() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to login page
        page.goto("https://missionpeak.app/account")
        # Login
        page.get_by_label("Email address").fill("swatidhoke@gmail.com")
        page.get_by_label("Password").fill("missionPeak1!")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Okay").click()
        # Add post
        page.get_by_role("button", name="add", exact=True).click()
        page.locator("a", has_text="Post Broadcast something").click()
        editor = page.locator("p-editor div").nth(3)
        editor.click()
        editor.fill("my playwright create post test")
        # Select location
        page.get_by_text("location_on").click()
        page.wait_for_timeout(10000)
        page.get_by_placeholder("Enter Location").fill("northwest ymca")
        page.wait_for_timeout(10000)
        page.locator(".pac-item").first.click()
        page.wait_for_timeout(10000)
        page.get_by_role("button", name="Select Location").click()
        page.wait_for_timeout(10000)
        # Post
        page.get_by_role("button", name="Post").click()
        page.get_by_text("View Post").click()