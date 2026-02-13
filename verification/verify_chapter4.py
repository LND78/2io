import re
from playwright.sync_api import sync_playwright

def verify_chapter4():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the chapter page
        url = "http://localhost:3000/chapter/4"
        print(f"Navigating to {url}")
        page.goto(url)

        # 1. Verify Title
        print("Verifying Title...")
        title = page.locator("h1").first.text_content()
        print(f"Found title: {title}")
        assert "The Age of Industrialisation" in title

        hindi_title = page.locator("h2").first.text_content()
        print(f"Found Hindi title: {hindi_title}")
        assert "औद्योगीकरण का युग" in hindi_title

        # 2. Verify a specific MCQ (Q1)
        print("Verifying MCQ 1...")
        q1_text = page.locator("text=Who invented the Spinning Jenny?").first.text_content()
        assert "Who invented the Spinning Jenny?" in q1_text

        # Verify Hindi text is present (it usually renders as small text or subtitle)
        # We need to find the container that has Q1 text and check if it contains the Hindi text
        assert page.locator("text=स्पिनिंग जेनी का आविष्कार किसने किया?").count() > 0

        # Check if options are present
        assert page.locator("text=(b) James Hargreaves").count() > 0

        # Test Show Answer for MCQ
        print("Testing Show Answer for MCQ...")
        # Find the button associated with this question.
        # Since it's hard to target specific button by text, we'll verify the answer text appears after clicking.
        # We assume the first "Show Answer" button corresponds to the first question.
        show_answer_btns = page.locator("button:has-text('Show Answer')")
        show_answer_btns.first.click()

        # Verify answer is visible
        answer_text = page.locator("text=(b) James Hargreaves").first
        assert answer_text.is_visible()

        # 3. Verify a Short Answer Question (Q11 - first short answer)
        print("Verifying Short Answer Q11...")
        q11_text = page.locator("text=How was the life of workers affected by the abundance of labor in the market?").first.text_content()
        assert "abundance of labor" in q11_text

        # Test Show Answer for Short Answer
        # Click the last visible show answer button or specific one
        # Let's find the specific question container
        q11_container = page.locator(".border", has_text="How was the life of workers affected")
        q11_btn = q11_container.locator("button:has-text('Show Answer')")
        q11_btn.click()

        ans11_text = page.locator("text=badly").first
        assert ans11_text.is_visible()

        # 4. Verify Long/Short Answer from Page 13 (Q14)
        print("Verifying Q14 from Page 13...")
        q14_text = page.locator("text=What problems did Indian weavers face due to British industrialisation?").first.text_content()
        assert "Manchester imports" in page.content() # Check if answer content is loaded in DOM (might be hidden) or check question text

        print("Chapter 4 Verification Passed!")
        page.screenshot(path="verification/chapter4_verify.png")
        print("Screenshot saved to verification/chapter4_verify.png")
        browser.close()

if __name__ == "__main__":
    verify_chapter4()
