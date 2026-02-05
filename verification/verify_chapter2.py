from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Load the local HTML file
    page.goto("file:///app/index.html")

    # Click on Chapter 2 link
    page.click("a[href='#chapter2']")

    # Wait for the section to be visible
    chapter2_section = page.locator("#chapter2")
    expect(chapter2_section).to_be_visible()

    # Verify Header
    expect(page.locator("#chapter2 h2")).to_have_text("Chapter 2: Polynomials")

    # Verify Summary exists
    expect(page.locator("#chapter2 .summary")).to_be_visible()

    # Verify Question 1 exists
    expect(page.locator("#chapter2 .question-block").first).to_contain_text("Q1")

    # Click Show Answer for Q1
    # The button is the first button in the #chapter2 section
    show_answer_btn = page.locator("#chapter2 .question-block button").first
    show_answer_btn.click()

    # Verify Answer is visible
    answer_div = page.locator("#ch2-q1")
    expect(answer_div).to_be_visible()
    expect(answer_div).to_contain_text("Answer: (1)")

    # Take screenshot
    page.screenshot(path="verification/chapter2_verification.png", full_page=True)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
