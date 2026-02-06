from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Go to Home
        print("Navigating to home...")
        page.goto("http://localhost:3000")

        # 2. Check for Chapter 2
        print("Checking for Chapter 2...")
        chapter_link = page.get_by_text("Nationalism in India")
        expect(chapter_link).to_be_visible()

        # 3. Click Chapter 2
        print("Clicking Chapter 2...")
        chapter_link.click()

        # 4. Wait for navigation and check title
        print("Waiting for chapter page...")
        page.wait_for_url("**/chapter/2")
        expect(page.get_by_role("heading", name="Nationalism in India")).to_be_visible()

        # 5. Check for questions
        print("Checking for questions...")
        # Searching for a substring of the question text
        expect(page.get_by_text("Describe the Civil Disobedience Movement")).to_be_visible()

        # 6. Click Show Answer for Q1
        print("Toggling answer...")
        show_answer_btn = page.locator("button").filter(has_text="Show Answer").first
        show_answer_btn.click()

        # 7. Check Answer visibility
        print("Checking answer...")
        # Locate the answer text
        expect(page.get_by_text("Dandi March")).to_be_visible()

        # 8. Screenshot
        print("Taking screenshot...")
        page.screenshot(path="verification/chapter2_verify.png", full_page=True)

        browser.close()
        print("Done.")

if __name__ == "__main__":
    run()
