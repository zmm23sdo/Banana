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

def ReturnShipOrder(page, order_id,return_description):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=2
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=2")
    # Click text=1220419422410000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220419422410000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click .rounded.flex.justify-center
    page.locator(".rounded.flex.justify-center").click()
    # Click .w-full.h-10 >> nth=0
    page.locator(".w-full.h-10").first.click()
    # Click text=Return >> nth=3
    page.locator("text=Return").nth(3).click()
    # Click div:nth-child(7) .w-full
    page.locator("div:nth-child(7) .w-full").click()
    # Click text=Damage Upon Arrival
    page.locator("text=Damage Upon Arrival").click()
    # Fill textarea
    page.locator("textarea").fill(return_description)
    # Click text=Submit
    page.locator("text=Submit").click()

def RefundShipOrder(page, order_id, refund_description):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=2
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=2")
    # Click text=1220419422410000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220419422410000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click .rounded.flex.justify-center
    page.locator(".rounded.flex.justify-center").click()
    # Click .w-full.h-10 >> nth=0
    page.locator(".w-full.h-10").first.click()
    # Click text=Return >> nth=3
    page.locator("text=Refund").nth(3).click()
    # Click div:nth-child(7) .w-full
    page.locator("div:nth-child(7) .w-full").click()
    # Click text=Damage Upon Arrival
    page.locator("text=Damage Upon Arrival").click()
    # Fill textarea
    page.locator("textarea").fill(refund_description)
    # Click text=Submit
    page.locator("text=Submit").click()

def ReturnRefundShipOrder(page,order_id, returnrefund_description):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=2
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=2")
    # Click text=1220419422410000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220419422410000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click .rounded.flex.justify-center
    page.locator(".rounded.flex.justify-center").click()
    # Click .w-full.h-10 >> nth=0
    page.locator(".w-full.h-10").first.click()
    # Click text=Return >> nth=3
    page.locator("text=Return&Refund").click()
    # Click div:nth-child(7) .w-full
    page.locator("div:nth-child(7) .w-full").click()
    # Click text=Damage Upon Arrival
    page.locator("text=Damage Upon Arrival").click()
    # Fill textarea
    page.locator("textarea").fill(returnrefund_description)
    # Click text=Submit
    page.locator("text=Submit").click()

def DeliveryConfirmed(page, order_id):
    # Go to https://client-banana-dev.chunsutech.com/management/order/list?type=3
    page.goto("https://client-banana-dev.chunsutech.com/management/order/list?type=3")
    # Click text=1220426456170000001
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/detail?id=1220426456170000001"):
    with page.expect_navigation():
        page.locator("text="+order_id).click()
    # Click text=Delivery Confirmed
    page.locator("text=Delivery Confirmed").click()
    # Click span:has-text("Confirm")
    page.locator("span:has-text(\"Confirm\")").click()
    # Click .h-44px
    page.locator(".h-44px").click()
