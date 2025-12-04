
from playwright.sync_api import sync_playwright, expect
import os
import re

def verify_cheatsheet(page):
    # Load the HTML file
    file_path = os.path.abspath("dax-energy-cheatsheet.html")
    page.goto(f"file://{file_path}")

    # Wait for page readiness
    page.wait_for_timeout(1000)

    # 1. Take a screenshot of the Hero section (Full page initial state)
    page.screenshot(path="verification/dax_hero.png")

    # 2. Test Search Functionality (Verify Fix)
    search_input = page.locator("#global-search")
    search_input.fill("SUM")
    search_input.dispatch_event("input")

    # Wait for filter
    page.wait_for_timeout(1000)

    # Verify Contexto card is HIDDEN
    # Contexto card has text "Contexto" and keywords without "sum"
    # We find the specific card
    contexto_card = page.locator('.card.search-item').filter(has_text="Contexto").first

    # It should have class 'hidden'
    expect(contexto_card).to_have_class(re.compile(r"hidden"))

    # Verify SUM card is VISIBLE
    sum_card = page.locator('.card.search-item').filter(has_text="Producción Total").first
    expect(sum_card).not_to_have_class(re.compile(r"hidden"))

    # Take screenshot of filtered view
    page.screenshot(path="verification/dax_search_sum.png")
    print("Verification screenshots generated.")

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_cheatsheet(page)
        except Exception as e:
            print(f"Verification failed: {e}")
            raise e
        finally:
            browser.close()
