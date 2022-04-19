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
    with page.expect_navigation():
        page.locator("[placeholder=\"Search\\ Product\"]").fill(admin_productname)
    # Click text=Search
    page.locator("#root-box > div.h-60px.flex.justify-around.items-center.pl-2.pr-0\.5.bg-white > div.min-w-min.p-2\.5.cursor-pointer > div").click()

def SearchOrder(page, admin_productname):
    # Go to https://client-banana-dev.chunsutech.com/management
    page.goto("https://client-banana-dev.chunsutech.com/management")
    # Click text=View All >
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/list?type=0"):
    with page.expect_navigation():
        page.locator("text=View All >").click()
    # Click [placeholder="Search\ Order"]
    page.locator("[placeholder=\"Search\\ Order\"]").click()
    # Fill [placeholder="Search\ Order"]
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/order/search?s=text%3DProduct2022-04-19+11%3A45%3A48"):
    with page.expect_navigation():
        page.locator("[placeholder=\"Search\\ Order\"]").fill(admin_productname)
    # Click text=Search
    page.locator("text=Search").click()
    with page.expect_navigation():
        page.locator("#scrollElement > div > div > div.za-pull__body > div > a:nth-child(1) > div > div.pb-4.w-full.flex.flex-row.items-center.justify-between > div.flex-1.text-lg.text-normal.text-opacity-70 > div.inline.text-normal").first.hover()