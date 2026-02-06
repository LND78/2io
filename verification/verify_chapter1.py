from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Go to Home
        print("Navigating to home...")
        page.goto("http://localhost:3000")

        # 2. Check for Chapter 1
        print("Checking for Chapter 1...")
        chapter_link = page.get_by_text("The Rise of Nationalism in Europe")
        expect(chapter_link).to_be_visible()

        # 3. Click Chapter 1
        print("Clicking Chapter 1...")
        chapter_link.click()

        # 4. Wait for navigation and check title
        print("Waiting for chapter page...")
        page.wait_for_url("**/chapter/1")
        expect(page.get_by_role("heading", name="The Rise of Nationalism in Europe")).to_be_visible()

        # 5. Check for questions
        print("Checking for questions...")
        expect(page.get_by_text("Who was the father of the process of nation-state formation in Germany?")).to_be_visible()

        # 6. Click Show Answer for Q1
        print("Toggling answer...")
        show_answer_btn = page.locator("button").filter(has_text="Show Answer").first
        show_answer_btn.click()

        # 7. Check Answer visibility
        print("Checking answer...")
        # Locate the answer container that appears after clicking
        answer_container = page.locator("div").filter(has_text="Answer:").last
        expect(answer_container).to_be_visible()
        expect(answer_container).to_contain_text("Otto von Bismarck")

        # 8. Screenshot
        print("Taking screenshot...")
        page.screenshot(path="verification/chapter1_verify.png", full_page=True)

        browser.close()
        print("Done.")

if __name__ == "__main__":
    run()
