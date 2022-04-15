def CreateProductBasic(page, admin_prouctname, admin_product_description, admin_product_price, admin_product_stock,
                       admin_product_weight, admin_product_freight
    ):
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
    
def CreateProductAdvance(page, admin_prouctname, admin_product_description, admin_product_brand, admin_variation0,
                         admin_option0, admin_variation1, admin_option3, admin_product_price,
                         admin_product_stock, admin_product_weight, admin_product_sku, admin_product_barcode
    ):
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
    # Upload /Users/michaelcheung/Project/Banana/pic.jpeg
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0001.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0002.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0003.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0004.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0005.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0006.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0007.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0008.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0009.jpg")
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/Pictures/0010.jpg")
    # Click .ant-select-selection-overflow >> nth=0
    page.locator(".ant-select-selection-overflow").first.click()
    # Click .ant-select-tree-checkbox-inner >> nth=0
    page.locator(".ant-select-tree-checkbox-inner").first.click()
    # Fill text=品牌Warranty Duration请选择Warranty Type请选择Suitable vehicle brand 请选择 >> [placeholder="请输入"]
    page.locator("text=品牌Warranty Duration请选择Warranty Type请选择Suitable vehicle brand 请选择 >> [placeholder=\"请输入\"]").fill(admin_product_brand)
    # Click text=Warranty Duration请选择 >> input[role="combobox"]
    page.locator("text=Warranty Duration请选择 >> input[role=\"combobox\"]").click()
    # Click .ant-select-item >> nth=0
    page.locator(".ant-select-item").first.click()
    # Click text=Warranty Type请选择 >> input[role="combobox"]
    page.locator("text=Warranty Type请选择 >> input[role=\"combobox\"]").click()
    # Click text=Supplier Warranty >> nth=1
    page.locator("text=Supplier Warranty").nth(1).click()
    # Click .ant-select.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-multiple .ant-select-selector
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div:nth-child(6) > div.ant-space.ant-space-vertical.ant-space-align-start.ant-pro-form-group-container > div:nth-child(2) > div > div:nth-child(3) > div.ant-col.ant-form-item-control > div > div > div > div > div").click()
    # Click text=Ford
    page.locator("text=Ford").click()
    # Click text=Suitable vehicle brand
    page.locator("text=Suitable vehicle brand").click()
    # Click button:has-text("Enable Variation")
    page.locator("button:has-text(\"Enable Variation\")").click()
    # Click text=Variation >> nth=0
    page.locator("text=Variation").first.click()
    # Fill [placeholder="Enter\ Vairation\ Name\,eg\:colour\,etc\."]
    page.locator("[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:colour\\,etc\\.\"]").fill(admin_variation0)
    # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=0
    page.locator("[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]").first.fill(admin_option0)
    page.set_input_files('input[id^="testpic_"]',"/Users/michaelcheung/Project/Banana/Pictures/0011.jpg")
    # Click button:has-text("Add Variation")
    page.locator("button:has-text(\"Add Variation\")").click()
    # Click span:has-text("Variation1")
    page.locator("span:has-text(\"Variation1\")").click()
    # Click text=Variation1OptionsAdd Options >> [placeholder="Enter\ Vairation\ Name\,eg\:colour\,etc\."]
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div:nth-child(7) > div.ant-space.ant-space-vertical.ant-space-align-start.ant-pro-form-group-container > div > div > div > div:nth-child(2) > div.ant-row.ant-form-item > div > div > div > span > input").click()
    # Click text=Variation1OptionsAdd Options
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div:nth-child(7) > div.ant-space.ant-space-vertical.ant-space-align-start.ant-pro-form-group-container > div > div > div > div:nth-child(2) > div.ant-row.ant-form-item > div > div > div > span > input").fill(admin_variation1)
    # Fill text=Variation1OptionsAdd Options >> [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."]
    page.locator("text=Variation1OptionsAdd Options >> [placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]").fill(admin_option3)
    # Fill [placeholder="Price"]
    page.locator("[placeholder=\"Price\"]").fill(admin_product_price)
    # Fill [placeholder="Stock"]
    page.locator("[placeholder=\"Stock\"]").fill(admin_product_stock)
    # Fill [placeholder="Weight"]
    page.locator("[placeholder=\"Weight\"]").fill(admin_product_weight)
    # Fill [placeholder="SKU"]
    page.locator("[placeholder=\"SKU\"]").fill(admin_product_sku)
    # Fill [placeholder="Bar\ Code"]
    page.locator("[placeholder=\"Bar\\ Code\"]").fill(admin_product_barcode)
    # Click button:has-text("Apply To All")
    page.locator("button:has-text(\"Apply To All\")").click()
    # Click input[type="radio"] >> nth=2
    page.locator("input[type=\"radio\"]").nth(2).click()
    # Click .ant-select.ant-select-status-error .ant-select-selector
    page.locator("text=Freight Template请选择 >> input[role=\"combobox\"]").click()
    # Click .ant-select-dropdown.ant-select-dropdown-placement-topLeft div div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active
    page.locator(".ant-select-dropdown.ant-select-dropdown-placement-topLeft div div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active").click()
    
    # Click text=Place of shipment请选择 >> input[role="combobox"]
    page.locator("text=Place of shipment请选择 >> input[role=\"combobox\"]").click()
    # Click text=Terengganu >> nth=1
    page.locator("text=Terengganu").nth(1).click()

    # Click button:has-text("Save and Publish")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/commodity/list"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Save and Publish\")").click()

def ChangeProduct(page, admin_prouctname, admin_new_prouctname, admin_new_product_description):
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_prouctname)
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Change")
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.table___1mj95 > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > button > span").click()
    # Fill text=Product Name32 / 120 >> [placeholder="请输入"]
    page.locator("#name").fill(admin_new_prouctname)
    # Fill text=Product Description: Product2022-04-14 15:18:38 2022-04-14 15:18:38
    page.locator("#describe").fill(admin_new_product_description)
    # Click button:has-text("Save and Publish")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/commodity/list"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Save and Publish\")").click()
