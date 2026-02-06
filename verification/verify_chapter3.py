import re
from playwright.sync_api import sync_playwright

def verify_chapter3():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go directly to Chapter 3
        # Since the server is running, and we just added the file, Next.js should have picked it up.
        # However, getAllChapters might be static or cached if using getStaticProps without revalidate,
        # but here we are likely using dynamic or the dev server.

        page.goto("http://localhost:3000/chapter/3")
        page.wait_for_load_state("networkidle")
        print("Navigated to Chapter 3.")

        # Verify Title
        if page.is_visible("text=भूमण्डलीकृत विश्व का बनना"):
            print("Title Verified.")
        else:
            print("Title NOT found.")

        # Verify MCQ Question 1 content
        # Question: "1885 में यूरोप के ताकतवर देशों ने..."
        if page.is_visible("text=1885 में यूरोप के ताकतवर देशों"):
            print("MCQ 1 Verified.")
        else:
            print("MCQ 1 NOT found.")

        # Verify Essay Question (Silk Route)
        if page.is_visible("text=रेशम मार्ग से किन-किन वस्तुओं का व्यापार होता था"):
            print("Essay Question Verified.")
        else:
            print("Essay Question NOT found.")

        # Verify Show Answer functionality
        # Find a "Show Answer" button. There are multiple. Pick the first one.
        buttons = page.locator("button:has-text('Show Answer')")
        if buttons.count() > 0:
            buttons.first.click()
            print("Clicked first Show Answer button.")

            # The answer for the first MCQ is "अफ्रीका (Africa)"
            # Wait a moment for state update if necessary (usually instant in React)
            page.wait_for_timeout(500)

            if page.is_visible("text=अफ्रीका"):
                print("Answer revealed successfully.")
            else:
                print("Answer text NOT found after click.")
        else:
            print("No 'Show Answer' buttons found.")

        browser.close()

if __name__ == "__main__":
    verify_chapter3()
