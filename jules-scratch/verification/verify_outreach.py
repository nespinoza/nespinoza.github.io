from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        html_file_path = os.path.abspath('outreach/index.html')
        page.goto(f'file://{html_file_path}')
        page.screenshot(path='jules-scratch/verification/verification.png', full_page=True)
        browser.close()

if __name__ == "__main__":
    run()