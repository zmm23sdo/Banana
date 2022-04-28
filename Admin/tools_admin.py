def CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price):
    # Go to https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers
    page.goto("https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # assert page.url == "https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers/create"
    # Click [placeholder="Voucher\ name\ is\ not\ visible\ to\ buyers"]
    page.locator("[placeholder=\"Voucher\\ name\\ is\\ not\\ visible\\ to\\ buyers\"]").click()
    # Fill [placeholder="Voucher\ name\ is\ not\ visible\ to\ buyers"]
    page.locator("[placeholder=\"Voucher\\ name\\ is\\ not\\ visible\\ to\\ buyers\"]").fill(voucher_name)
    # Click [placeholder="Please\ enter\ A-Z\,0-9\;10\ characters\ maximum"]
    page.locator("[placeholder=\"Please\\ enter\\ A-Z\\,0-9\\;10\\ characters\\ maximum\"]").click()
    # Fill [placeholder="Please\ enter\ A-Z\,0-9\;10\ characters\ maximum"]
    page.locator("[placeholder=\"Please\\ enter\\ A-Z\\,0-9\\;10\\ characters\\ maximum\"]").fill(voucher_code)
    # Click #time
    page.locator("#time").click()
    # Click .ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner >> nth=0
    page.locator(".ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner").first.click()
    # Click button:has-text("Ok")
    page.locator("button:has-text(\"Ok\")").click()
    # Click text=30 >> nth=1
    page.locator("text=30").nth(1).click()
    # Click button:has-text("Ok")
    page.locator("button:has-text(\"Ok\")").click()
    # Click text=By percentage% OFF >> [placeholder="请输入"]
    page.locator("text=By percentage% OFF >> [placeholder=\"请输入\"]").click()
    # Fill text=By percentage% OFF >> [placeholder="请输入"]
    page.locator("text=By percentage% OFF >> [placeholder=\"请输入\"]").fill(amount)
    # Click #publish_count
    page.locator("#publish_count").click()
    # Fill #publish_count
    page.locator("#publish_count").fill(usage_quantity)
    # Click text=Minimum Basket PriceRM >> [placeholder="请输入"]
    page.locator("text=Minimum Basket PriceRM >> [placeholder=\"请输入\"]").click()
    # Fill text=Minimum Basket PriceRM >> [placeholder="请输入"]
    page.locator("text=Minimum Basket PriceRM >> [placeholder=\"请输入\"]").fill(min_price)
    # Click button:has-text("提 交")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def CreateVoucherAmount(page,voucher_name, voucher_code, amount, usage_quantity,min_price):
    # Go to https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers
    page.goto("https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # assert page.url == "https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers/create"
    # Click [placeholder="Voucher\ name\ is\ not\ visible\ to\ buyers"]
    page.locator("[placeholder=\"Voucher\\ name\\ is\\ not\\ visible\\ to\\ buyers\"]").click()
    # Fill [placeholder="Voucher\ name\ is\ not\ visible\ to\ buyers"]
    page.locator("[placeholder=\"Voucher\\ name\\ is\\ not\\ visible\\ to\\ buyers\"]").fill(voucher_name)
    # Click [placeholder="Please\ enter\ A-Z\,0-9\;10\ characters\ maximum"]
    page.locator("[placeholder=\"Please\\ enter\\ A-Z\\,0-9\\;10\\ characters\\ maximum\"]").click()
    # Fill [placeholder="Please\ enter\ A-Z\,0-9\;10\ characters\ maximum"]
    page.locator("[placeholder=\"Please\\ enter\\ A-Z\\,0-9\\;10\\ characters\\ maximum\"]").fill(voucher_code)
    # Click #time
    page.locator("#time").click()
    # Click .ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner >> nth=0
    page.locator(".ant-picker-cell.ant-picker-cell-start .ant-picker-cell-inner").first.click()
    # Click button:has-text("Ok")
    page.locator("button:has-text(\"Ok\")").click()
    # Click text=30 >> nth=1
    page.locator("text=30").nth(1).click()
    # Click button:has-text("Ok")
    page.locator("button:has-text(\"Ok\")").click()
    # Click text=By percentage
    page.locator("text=By percentage").click()
    # Click text=Fix amount
    page.locator("text=Fix amount").click()
    # Click text=Fix amountRM >> [placeholder="请输入"]
    page.locator("text=Fix amountRM >> [placeholder=\"请输入\"]").click()
    # Fill text=Fix amountRM >> [placeholder="请输入"]
    page.locator("text=Fix amountRM >> [placeholder=\"请输入\"]").fill(amount)
    # Click #publish_count
    page.locator("#publish_count").click()
    # Fill #publish_count
    page.locator("#publish_count").fill(usage_quantity)
    # Click text=Minimum Basket PriceRM >> [placeholder="请输入"]
    page.locator("text=Minimum Basket PriceRM >> [placeholder=\"请输入\"]").click()
    # Fill text=Minimum Basket PriceRM >> [placeholder="请输入"]
    page.locator("text=Minimum Basket PriceRM >> [placeholder=\"请输入\"]").fill(min_price)
    # Click button:has-text("提 交")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def DeleteVoucher(page):
    # Go to https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers
    page.goto("https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers")
    # Click text=A2041Amount1651126701Shop Voucherall productsRM test1004/01/2022 14:18:38 - 04/3 >> button >> nth=1
    page.locator("button:nth-child(3) > span").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()
    page.goto("https://admin-banana-dev.chunsutech.com/marketing/tools/vouchers")
    page.locator(".ant-table-container > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1)").click()