def SearchReturnOrder(page, order_id):
    # Go to https://admin-banana-dev.chunsutech.com/order/refund
    page.goto("https://admin-banana-dev.chunsutech.com/order/refund")
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Review")
    page.locator("#antdTable > tbody > tr:nth-child(3) > td:nth-child(5) > button > span").click()
    # Click text=1220420549100000001
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)").click()