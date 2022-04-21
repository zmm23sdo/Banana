

def BuyProduct(page):
    page.locator(".absolute img").first.click()
    # Click text=Buy Now
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/shop/item?id=220314751950000001"):
    with page.expect_navigation():
        page.locator("text=Buy Now").click()
    # Click .rounded.flex.justify-center.items-center.bg-send
    page.locator(".rounded.flex.justify-center.items-center.bg-send").click()
    # Click text=General
    page.locator("text=General").click()
    # Click #select_drawer div:has-text("Buy Now") >> nth=2
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/cart/order"):
    page.locator("#select_drawer div:has-text(\"Buy Now\")").nth(2).click()
    with page.expect_navigation():
        # Click text=Place Order
        page.locator("text=Place Order").click()
    # Click text=field Signature is not set
    page.locator("text=field Signature is not set").click()

def CartProduct(page):
    page.locator(".absolute img").first.click()
    # Click #root-box div:has-text("Add To Cart") >> nth=2
    with page.expect_navigation():
        page.locator("#root-box div:has-text(\"Add To Cart\")").nth(2).click()
    # Click .rounded.flex.justify-center.items-center.bg-send
    page.locator(".rounded.flex.justify-center.items-center.border").click()
    # Click text=General
    page.locator("text=General").click()
    # Click #select_drawer div:has-text("Add To Cart") >> nth=2
    page.locator("#select_drawer div:has-text(\"Add To Cart\")").nth(2).click()
    # Click div[role="alert"]:has-text("Add to cart successfully")
    page.locator("div > div > div.MuiAlert-message.css-1w0ym84").click()
