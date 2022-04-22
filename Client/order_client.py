def CancelUnpaidOrder(page, order_id):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=1
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=1")
    # Click text=1220419422410000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220419422410000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click .rounded.flex.justify-center >> nth=0
    page.locator(".rounded.flex.justify-center").first.click()
    # Click div[role="dialog"] div:has-text("Submit") >> nth=2
    page.locator("div[role=\"dialog\"] div:has-text(\"Submit\")").nth(2).click()
    # Click text=Canceled
    page.locator("#root-box > div.h-44px.flex.justify-around.items-center.px-2.bg-white > div.flex-1.text-normal.text-xxl.text-center.flex.flex-col").click()

def GetOrderId(page,admin_productname):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=0
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=0")
    # Click .p-1
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/search"):
    with page.expect_navigation():
        page.locator(".p-1").click()
    # Fill [placeholder="Search\ Order"]
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/search?s=text%3DProduct2022-04-19+11%3A45%3A48"):
    with page.expect_navigation():
        page.locator("[placeholder=\"Search\\ Order\"]").fill(admin_productname)
    page.locator("#root-box > div.h-60px.flex.justify-around.items-center.pl-2.pr-0\.5.bg-white > div.min-w-min.p-2\.5.cursor-pointer > div").click()
    page.locator("#scrollElement > div > div > div.za-pull__body > div > a > div > div.pb-4.w-full.flex.flex-row.items-center.justify-between > div.flex-1.text-lg.text-normal.text-opacity-70 > div.inline.text-normal").hover
    order_no = page.text_content("#scrollElement > div > div > div.za-pull__body > div > a > div > div.pb-4.w-full.flex.flex-row.items-center.justify-between > div.flex-1.text-lg.text-normal.text-opacity-70 > div.inline.text-normal")
    order_id = str(order_no)
    return order_id

def PaynowUnpaidOrder(page, order_id):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=1
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=1")
    # Click text=1220419422410000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220419422410000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click text=Pay Now
    page.locator("text=Pay Now").click()
    # Click text=field Signature is not set
    page.locator("text=field Signature is not set").click()