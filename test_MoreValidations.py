import time

from playwright.sync_api import Page, expect


def test_UIChecks(page : Page):

    #hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible() #Making sure the display is visable
    page.get_by_role("button", name="Hide").click() #hiding display by clicking
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name = "Confirm").click()
    #time.sleep(3)


    #MouseHover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top")

    #Frame Handling
    pageFrame = page.frame_locator("#courses-iframe") #find iframe
    pageFrame.get_by_role("link", name="All Access plan").click() #click on page
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    #Check the price of rice is equal to 37
    #identify the price column
    #identify rice row
    #extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            print(f"Price column value is {priceColValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Discount price").count()>0:
            discountColValue = index
            print(f"Discount colum value is {discountColValue}")
            break

    potatoRow = page.locator("tr").filter(has_text="Potato")
    expect(potatoRow.locator("td").nth(discountColValue)).to_have_text("22")