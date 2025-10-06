from playwright.sync_api import Page, expect
import os

def test_header_no_twitter(page: Page):
    """
    This test verifies that the Twitter logo and link are not present in the header.
    """
    # 1. Arrange: Go to the index page.
    # The path needs to be absolute.
    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")

    # 2. Assert: Check that the twitter link is not present.
    # The link had the URL "https://twitter.com/nespinozap"
    twitter_link = page.locator('a[href="https://twitter.com/nespinozap"]')
    expect(twitter_link).to_have_count(0)

    # 3. Screenshot: Capture the header for visual verification.
    header = page.locator("header")
    header.screenshot(path="jules-scratch/verification/verification.png")