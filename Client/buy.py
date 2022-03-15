def buy_unlog(page):
   # Go to https://client-banana-test.chunsutech.com/home
    page.goto("https://client-banana-test.chunsutech.com/home")
    # Click button:has-text("Category")
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/category"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Category\")").click()
    # Click text=ExteriorInteriorAutomotive ToolsAudio & AlarmLightingAccessoriesWiper >> img
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/category/1?cid=7&bid=&sort="):
    with page.expect_navigation():
        page.locator("text=ExteriorInteriorAutomotive ToolsAudio & AlarmLightingAccessoriesWiper >> img").click()
    # Click text=22222222222222222222RM 2222.00Sold: 2
   
   
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/shop/item?id=220314751950000001"):
    with page.expect_navigation():
        page.locator("#scrollElement > div > div > div.za-pull__body > div > div:nth-child(1)").click()

        
    # Click .rounded.flex.justify-center.items-center.bg-send
    page.locator(".rounded.flex.justify-center.items-center.bg-send").click()
    # Click div[role="presentation"] >> text=22222222222222222222
   
   
    page.locator("div[role=\"presentation\"] >> text=22222222222222222222").click()
    # Click #select_drawer div:has-text("Buy Now") >> nth=2
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/user?redirection=/shop/item&id=220314751950000001"):
    with page.expect_navigation():
        page.locator("#select_drawer div:has-text(\"Buy Now\")").nth(2).click()
    # Click input[name="phoneNumber"]
    page.locator("input[name=\"phoneNumber\"]").click()
    # Fill input[name="phoneNumber"]
    page.locator("input[name=\"phoneNumber\"]").fill("8615195927818")
    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("qwer`123")
    # Click text=Submit
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/shop/item?id=220314751950000001"):
    with page.expect_navigation():
        page.locator("text=Submit").click()
    # Click .rounded.flex.justify-center.items-center.bg-send
    page.locator(".rounded.flex.justify-center.items-center.bg-send").click()
    # Click div[role="presentation"] >> text=22222222222222222222
    page.locator("div[role=\"presentation\"] >> text=22222222222222222222").click()
    # Click #select_drawer div:has-text("Buy Now") >> nth=2
    # with page.expect_navigation(url="https://client-banana-test.chunsutech.com/cart/order"):
    with page.expect_navigation():
        page.locator("#select_drawer div:has-text(\"Buy Now\")").nth(2).click()
    # Click text=Place Order
    page.locator("text=Place Order").click()