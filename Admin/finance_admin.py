def CompletedToPay(page, return_id, actual_amount):
    # Go to https://admin-banana-dev.chunsutech.com/finance/topay/
    page.goto("https://admin-banana-dev.chunsutech.com/finance/topay/")
    # Click [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").click()
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(return_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Completed")
    page.locator(".ant-table-container > div > table > tbody > tr > td:nth-child(6) > button > span").first.click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(actual_amount)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(return_id)
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click td:has-text("completed")
    page.locator("td:nth-child(5)").click()