from email.policy import default

import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help = "browser selection")
    parser.addoption("--url_name", action="store", default="https://rahulshettyacademy.com/client", help="URL selection")

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    broswer_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if broswer_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif broswer_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()