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

def AgreeReturnOrder(page, order_id):
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
    # Click button:has-text("Agree To Return/Refund")
    page.locator("button:has-text(\"Agree To Return/Refund\")").click()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click text=To Respond
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B").click()

def RejectReturnOrder(page, order_id, reject_reson):
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
    # Click button:has-text("Reject")
    page.locator("button:has-text(\"Reject\")").click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(reject_reson)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click text=To Respond
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B").click()

def ConfirmReceiptRetunOrder(page, order_id):
    # Go to https://admin-banana-dev.chunsutech.com/order/refund
    page.goto("https://admin-banana-dev.chunsutech.com/order/refund")
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Return/Refund Details")
    page.locator("#antdTable > tbody > tr:nth-child(3) > td:nth-child(5) > div > button:nth-child(2) > span").click()
    # Click button:has-text("Confirm Receipt")
    page.locator("button:has-text(\"Confirm Receipt\")").click()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click text=Request Completed
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B").click()

def CancelReceiptRetunOrder(page, order_id, cancel_reson):
    # Go to https://admin-banana-dev.chunsutech.com/order/refund
    page.goto("https://admin-banana-dev.chunsutech.com/order/refund")
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Return/Refund Details")
    page.locator("#antdTable > tbody > tr:nth-child(3) > td:nth-child(5) > div > button:nth-child(2) > span").click()
    # Click button:has-text("Cancel")
    page.locator("button:has-text(\"Cancel\")").click()
     # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(cancel_reson)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click text=Request Completed
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B").click()


def ArrageShipment(page, order_id, ship_company_id, ship_no):
    # Go to https://admin-banana-dev.chunsutech.com/order/list
    page.goto("https://admin-banana-dev.chunsutech.com/order/list")
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Arrange Shipment")
    page.locator(".ant-btn.ant-btn-default.tableOperationBtn___BlEiX").first.click()
    # Fill #ship_company_id
    page.locator("#ship_company_id").fill(ship_company_id)
    # Fill #ship_no
    page.locator("#ship_no").fill(ship_no)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click .ant-message-custom-content
    page.locator(".ant-message-custom-content").click()

def ChangeOrderTotal(page, order_id, total_price, ship_price):
    # Go to https://admin-banana-dev.chunsutech.com/order/list/
    page.goto("https://admin-banana-dev.chunsutech.com/order/list/")
    # Click [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").click()
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Change Order Total")
    page.locator(".ant-btn.ant-btn-default.tableOperationBtn___BlEiX").first.click()
    # Fill text=一口价RM >> [placeholder="请输入"]
    page.locator("text=一口价RM >> [placeholder=\"请输入\"]").fill(total_price)
    # Fill text=邮费RM >> [placeholder="请输入"]
    page.locator("text=邮费RM >> [placeholder=\"请输入\"]").fill(ship_price)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def GetReturnId(page,order_id):
     # Go to https://admin-banana-dev.chunsutech.com/order/refund/
    page.goto("https://admin-banana-dev.chunsutech.com/order/refund/")
    # Click [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").click()
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator("[placeholder=\"选择属性项搜索，或者输入关键字识别搜索\"]").fill(order_id)
    # Click .ant-btn >> nth=0
    page.locator(".ant-btn").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Return/Refund Details")
    page.locator("#antdTable > tbody > tr:nth-child(3) > td:nth-child(5) > button > span").click()
    # assert page.url == "https://admin-banana-dev.chunsutech.com/order/refund/detail?id=2220425361520000001"
    # Click text=2220425361520000001
    page.locator(".detailIds___b3ust > div:nth-child(1) > div:nth-child(2)").click()
    content = page.text_content(".detailIds___b3ust > div:nth-child(1) > div:nth-child(2)")
    return_id = str(content)
    return return_id