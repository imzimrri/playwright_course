# from playwright.sync_api import sync_playwright
import time

from playwright.sync_api import Page, expect, Playwright


# def test_playwrightBasics():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://rahulshettyacademy.com")

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning_wrong")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    #Incorect password or username
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowser(playwright:Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless= False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning_wrong")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # Incorect password or username
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()