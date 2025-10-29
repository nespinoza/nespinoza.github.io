from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8000/2025/10/27/using-ray.html")
    code_block = page.query_selector(".highlight")
    code_block.screenshot(path="jules-scratch/verification/code_block.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
