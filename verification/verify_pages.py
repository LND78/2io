from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # 1. Home Page
    print("Navigating to Home Page")
    page.goto("http://localhost:3000")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="verification/home.png")
    print("Screenshot home.png saved")

    # 2. Navigate to History
    print("Navigating to History")
    page.click("text=History")
    page.wait_for_url("http://localhost:3000/history")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="verification/history.png")
    print("Screenshot history.png saved")

    # 3. Navigate to Chapter 1
    print("Navigating to Chapter 1")
    # Using a more specific selector if needed, but text should work if unique enough
    page.click("text=Chapter 1")
    page.wait_for_url("http://localhost:3000/history/1")
    page.wait_for_load_state("networkidle")

    # 4. Toggle Answer
    print("Toggling Answer")
    # Click the first "Show Answer" button
    page.click("button:has-text('Show Answer') >> nth=0")

    # Wait for answer to appear (animation might take a moment, but playwright usually waits for visibility)
    page.wait_for_selector("text=Ans.")

    page.screenshot(path="verification/chapter_with_answer.png", full_page=True)
    print("Screenshot chapter_with_answer.png saved")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
