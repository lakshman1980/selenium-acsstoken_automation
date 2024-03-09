import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto('https://www.google.com/')

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

#playwright codegen demo.playwright.dev/todomvc
#https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id=513de26d-bc67-493a-a0be-4d8e463b3f56&redirect_uri=https%3A%2F%2Fwww.google.com%2F
#e1lVkX


