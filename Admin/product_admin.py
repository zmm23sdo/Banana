def CreateProductBasic(page, admin_prouctname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight):
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # assert page.url == "https://admin-banana-dev.chunsutech.com/commodity/list/create"
    # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
    page.locator("text=Product Name0 / 120 >> [placeholder=\"请输入\"]").fill(admin_prouctname)
     # Click text=Product Category请选择 >> input[role="combobox"]
    page.locator("text=Product Category请选择 >> input[role=\"combobox\"]").click()
    # Click text=Accessories >> nth=0
    page.locator("text=Accessories").first.click()
    # Click text=Screen Protectors
    page.locator("text=Screen Protectors").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill(admin_product_description)
    # Click span[role="button"]:has-text("单击上传")
    # page.locator("span[role=\"button\"]:has-text(\"单击上传\")").click()
    # Upload /Users/michaelcheung/Project/Banana/pic.jpeg
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/pic.jpeg")
    # Click .ant-select.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-multiple .ant-select-selector
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div:nth-child(6) > div.ant-space.ant-space-vertical.ant-space-align-start.ant-pro-form-group-container > div:nth-child(2) > div > div:nth-child(3) > div.ant-col.ant-form-item-control > div > div > div > div > div").click()
    # Click text=Ford
    page.locator("text=Ford").click()
    # Click text=Suitable vehicle brand
    page.locator("text=Suitable vehicle brand").click()
    # Fill text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").fill(admin_product_price)
    # Fill #stock
    page.locator("#stock").fill(admin_product_stock)
    # Fill text=Weightkg >> [placeholder="请输入"]
    page.locator("text=Weightkg >> [placeholder=\"请输入\"]").fill(admin_product_weight)
    # Fill text=Unified The FreightRM >> [placeholder="请输入"]
    page.locator("text=Unified The FreightRM >> [placeholder=\"请输入\"]").fill(admin_product_freight)
    # Click .ant-space div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.locator(".ant-space div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector").click()
    # Click .ant-select-dropdown.ant-select-dropdown-placement-topLeft div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active
    page.locator("body > div:nth-child(6) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div.ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active > div").click()
    # Click button:has-text("Save and Publish")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/commodity/list"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Save and Publish\")").click()
    