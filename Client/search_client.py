def SearchProduct(page, admin_productname):
    # Go to https://client-banana-dev.chunsutech.com/category
    page.goto("https://client-banana-dev.chunsutech.com/category")
    # Click text=Search Product
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/shop/search"):
    with page.expect_navigation():
        page.locator("text=Search Product").click()
    # assert page.url == "https://client-banana-dev.chunsutech.com/shop/search"
    # Click [placeholder="Search\ Product"]
    page.locator("[placeholder=\"Search\\ Product\"]").click()
    # Fill [placeholder="Search\ Product"]
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/shop/search?s=Product2022-04-18+15%3A31%3A41"):
    page.locator("[placeholder=\"Search\\ Product\"]").fill(admin_productname)
    # Click text=Search
    page.locator(".cursor-pointer > div").first.click()

def SearchOrder(page, admin_productname):
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
    # Click #root-box div:has-text("Search") >> nth=1
    page.locator("#root-box > div.h-60px.flex.justify-around.items-center.pl-2.pr-0\.5.bg-white > div.min-w-min.p-2\.5.cursor-pointer > div").click()
    