import json

# pytest -n 13 --tracing on --html=report.html
# pytest -n 13 --tracing retain-on-failure --html=report.html
# trace.playwright.dev
# if tracing ran with headless = False it won't generate a trace

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage

from pageObjects.dashboard import DashboardPage
from utils.apiBaseFramework import APIUtils

# Json file -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    user_email = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]


    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    #login
    loginPage = LoginPage(browserInstance) #Object for LoginPage class
    loginPage.navigate()
    dashboardPage = loginPage.login(user_email, user_password)

    #dashboard page
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailPage.verifyOrderMessage()



