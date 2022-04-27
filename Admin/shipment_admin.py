def SearchDelivery(page, module_name):
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(module_name)
    # Click button >> nth=2
    page.locator(".ant-input-group-addon").first.click()
    # Click text=第 0-0 条/总共 0 条
    page.locator("text="+module_name).click()
    
def CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw):
    # Go to https://admin-banana-dev.chunsutech.com/logistics/fee_management
    page.goto("https://admin-banana-dev.chunsutech.com/logistics/fee_management")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(module_name)
    # Click button:has-text("Choose Delivery Area")
    page.locator("button:has-text(\"Choose Delivery Area\")").click()
    # Check .ant-checkbox-input >> nth=0
    page.locator(".ant-checkbox-input").first.check()
    # Check label:nth-child(2) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(2) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(3) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(3) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(4) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(4) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(5) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(5) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(6) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(6) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(7) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(7) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(8) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(8) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(9) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(9) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(10) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(10) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(11) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(11) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(12) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(12) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(13) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(13) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(14) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(14) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(15) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(15) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(16) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(16) .ant-checkbox .ant-checkbox-input").check()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Fill [placeholder="请输入"] >> nth=1
    page.locator("[placeholder=\"请输入\"]").nth(1).fill(first_piece)
    # Fill [placeholder="请输入"] >> nth=2
    page.locator("[placeholder=\"请输入\"]").nth(2).fill(freight)
    # Fill [placeholder="请输入"] >> nth=3
    page.locator("[placeholder=\"请输入\"]").nth(3).fill(continuation)
    # Fill [placeholder="请输入"] >> nth=4
    page.locator("[placeholder=\"请输入\"]").nth(4).fill(rnenw)
    # Click text=保存
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div > form > div:nth-child(4) > div.ant-col.ant-form-item-control > div > div > div.ant-pro-table > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(6) > div").click()
    # Click button:has-text("提 交")
    # with page1.expect_navigation(url="https://admin-banana-dev.chunsutech.com/logistics/fee_management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()

def CreateDeliveryWeight(page, module_name, first_weight, freight, continued_weight, rnenw):
    # Go to https://admin-banana-dev.chunsutech.com/logistics/fee_management
    page.goto("https://admin-banana-dev.chunsutech.com/logistics/fee_management")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(module_name)
    # Click input[type="radio"] >> nth=1
    page.locator("input[type=\"radio\"]").nth(1).click()
    # Click button:has-text("Choose Delivery Area")
    page.locator("button:has-text(\"Choose Delivery Area\")").click()
    # Check .ant-checkbox-input >> nth=0
    page.locator(".ant-checkbox-input").first.check()
    # Check label:nth-child(2) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(2) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(3) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(3) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(4) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(4) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(5) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(5) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(6) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(6) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(7) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(7) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(8) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(8) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(9) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(9) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(10) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(10) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(11) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(11) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(12) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(12) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(13) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(13) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(14) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(14) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(15) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(15) .ant-checkbox .ant-checkbox-input").check()
    # Check label:nth-child(16) .ant-checkbox .ant-checkbox-input
    page.locator("label:nth-child(16) .ant-checkbox .ant-checkbox-input").check()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Fill [placeholder="请输入"] >> nth=1
    page.locator("[placeholder=\"请输入\"]").nth(1).fill(first_weight)
    # Fill [placeholder="请输入"] >> nth=2
    page.locator("[placeholder=\"请输入\"]").nth(2).fill(freight)
    # Fill [placeholder="请输入"] >> nth=3
    page.locator("[placeholder=\"请输入\"]").nth(3).fill(continued_weight)
    # Fill [placeholder="请输入"] >> nth=4
    page.locator("[placeholder=\"请输入\"]").nth(4).fill(rnenw)
    # Click text=保存
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div > form > div:nth-child(4) > div.ant-col.ant-form-item-control > div > div > div.ant-pro-table > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(6) > div").click()
    # Click button:has-text("提 交")
    # with page1.expect_navigation(url="https://admin-banana-dev.chunsutech.com/logistics/fee_management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()

def EditDelivery(page, module_change_name):
    # Edit
    page.locator(".ant-collapse-extra > div > a:nth-child(3)").first.click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(module_change_name)
    # Click text=Module Name
    page.locator("text=Module Name").click()
    # Click button:has-text("提 交")
    # with page1.expect_navigation(url="https://admin-banana-dev.chunsutech.com/logistics/fee_management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()

def DeleteDelivery(page):
    # Delete
    page.locator(".ant-collapse-extra > div > a:nth-child(4)").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def ModifyCalculateFee(page):
    # Go to https://admin-banana-dev.chunsutech.com/logistics/fee_management
    page.goto("https://admin-banana-dev.chunsutech.com/logistics/fee_management")
    # Click text=Modify
    page.locator("text=Modify").click()
    # Click input[type="radio"] >> nth=1
    page.locator("input[type=\"radio\"]").nth(1).click()
    # Click [aria-label="check"] svg
    page.locator("[aria-label=\"check\"] svg").click()
