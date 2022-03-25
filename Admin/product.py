import random



def create_group(page):

    page.goto("https://admin-banana-test.chunsutech.com/dashboard")

    # Click div[role="menuitem"]:has-text("Commodity")
    page.locator("div[role=\"menuitem\"]:has-text(\"Commodity\")").click()

    # # Click [id="rc-menu-uuid-71645-1-\/commodity-popup"] >> text=Commodity Category
    # page.locator("[id=\"rc-menu-uuid-71645-1-\\/commodity-popup\"] >> text=Commodity Category").click()

    # Click a:has-text("Commodity Category")
    page.locator("a:has-text(\"Commodity Category\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/commodity/category"
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill("test_group_000"+str(random.randint(0,9999)))
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    
def create_tran(page, tran_name):
    # Go to https://admin-banana-test.chunsutech.com/dashboard
    page.goto("https://admin-banana-test.chunsutech.com/dashboard")
    # Click span:has-text("Logistics") >> nth=0
    page.locator("span:has-text(\"Logistics\")").first.click()
    # Click a:has-text("Logistics Fee Management")·()
    # assert page.url == "https://admin-banana-test.chunsutech.com/logistics/fee_management"
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/logistics/fee_management/create_module"
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(tran_name)
    # Click input[type="radio"] >> nth=0
    page.locator("input[type=\"radio\"]").first.click()
    # Click button:has-text("Chosse Delivery Area")
    page.locator("button:has-text(\"Chosse Delivery Area\")").click()
    # Check .ant-checkbox-input >> nth=0
    page.locator(".ant-checkbox-input").first.check()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click text=保存
    page.locator("text=保存").click()
    # Click button:has-text("提 交")
    # with page.expect_navigation(url="https://admin-banana-test.chunsutech.com/logistics/fee_management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"提 交\")").click()

def create_prouct(page,product_name):

    page.goto("https://admin-banana-test.chunsutech.com/dashboard")

    # Click div[role="menuitem"]:has-text("Commodity")
    page.locator("div[role=\"menuitem\"]:has-text(\"Commodity\")").click()
    # Click a:has-text("Commodity List")
    page.locator("a:has-text(\"Commodity List\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/commodity/list"
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
    page.locator("text=Product Name0 / 120 >> [placeholder=\"请输入\"]").fill(product_name)
    page.locator("text=Product Category请选择 >> input[role=\"combobox\"]").click()
    # Click .anticon.anticon-right svg >> nth=0
    page.locator(".anticon.anticon-right svg").first.click()
    # Click text=Wiper
    page.locator("text=Wiper").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill("test_product_description_000"+str(random.randint(0,9999)))
    
    # with page.expect_navigation():
    page.set_input_files("input#pic","/Users/michaelcheung/Project/Banana/pic.jpeg")
    # waiting upload file finished:
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div.ant-row.ant-form-item.ant-form-item-has-success > div.ant-col.ant-form-item-control > div.ant-form-item-control-input > div > span > div > div.ant-upload.ant-upload-select.ant-upload-select-picture-card > span").wait_for()
    
    
    # Click .ant-select-selection-overflow >> nth=0
    page.locator(".ant-select-selection-overflow").first.click()
    
    # Click .ant-cascader-checkbox-inner >> nth=0
    page.locator(".ant-cascader-checkbox-inner").first.click()

    # Click .ant-select-selection-overflow >> nth=0
    page.locator(".ant-select-selection-overflow").first.click()
    # Fill text=品牌Warranty Duration请选择Warranty Type请选择Suitable vehicle brand 请选择Suitable vehicle >> [placeholder="请输入"]
    page.locator("text=品牌Warranty Duration请选择Warranty Type请选择Suitable vehicle brand 请选择Suitable vehicle >> [placeholder=\"请输入\"]").fill("test_brand_name_000"+str(random.randint(0,9999)))
    # Click text=Warranty Duration请选择 >> input[role="combobox"]
    page.locator("text=Warranty Duration请选择 >> input[role=\"combobox\"]").click()
    # Click text=1 Month >> nth=1
    page.locator("text=1 Month").nth(1).click()
    # Click text=Warranty Type请选择 >> input[role="combobox"]
    page.locator("text=Warranty Type请选择 >> input[role=\"combobox\"]").click()
    # Click text=Supplier Warranty >> nth=1
    page.locator("text=Supplier Warranty").nth(1).click()
    # Click .ant-select.ant-pro-filed-search-select .ant-select-selector .ant-select-selection-overflow >> nth=0
    page.locator(".ant-select.ant-pro-filed-search-select .ant-select-selector .ant-select-selection-overflow").first.click()

     # Click .ant-select-dropdown div div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active
    page.locator(".ant-select-dropdown div div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active").click()
     # Click .ant-space-item div div:nth-child(3) .ant-col.ant-form-item-label >> nth=0
    page.locator(".ant-space-item div div:nth-child(3) .ant-col.ant-form-item-label").first.click()
    
    # Click .ant-space-item div div:nth-child(4) .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector .ant-select-selection-overflow
    page.locator(".ant-space-item div div:nth-child(4) .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector .ant-select-selection-overflow").click()
   
    # Click div:nth-child(10) div .ant-select-dropdown div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item
    page.locator("div:nth-child(10) div .ant-select-dropdown div .rc-virtual-list .rc-virtual-list-holder div .rc-virtual-list-holder-inner .ant-select-item").click()

    # Click .ant-select.ant-select-status-success.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-focused .ant-select-selector .ant-select-selection-overflow
    page.locator(".ant-select.ant-select-status-success.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-focused .ant-select-selector .ant-select-selection-overflow").click()
    # Click text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").click()
    # Click text=PriceRM >> [placeholder="请输入"]
    # page.locator("text=PriceRM >> [placeholder=\"请输入\"]").click()
    # Double click text=PriceRM >> [placeholder="请输入"]
    # page.locator("text=PriceRM >> [placeholder=\"请输入\"]").dblclick()
    # Fill text=PriceRM >> [placeholder="请输入"]
    page.locator("#price").fill("100")
    # Click #stock
    page.locator("#stock").click()
    # Click .ant-input-affix-wrapper.ant-input-affix-wrapper-focused
    # page.locator(".ant-input-affix-wrapper.ant-input-affix-wrapper-focused").click()
    # Fill #stock
    page.locator("#stock").fill("100")
    # Click text=Weightkg >> [placeholder="请输入"]
    page.locator("text=Weightkg >> [placeholder=\"请输入\"]").click()
    # Fill text=Weightkg >> [placeholder="请输入"]
    page.locator("#weight").fill("100")
    # Click #admin_sku
    page.locator("#admin_sku").click()
    # Fill #admin_sku
    page.locator("#admin_sku").fill("test_spu_00001")
    # Click #barcode
    page.locator("#barcode").click()
    # Fill #barcode
    page.locator("#barcode").fill("test_brandcode_00001")
    # Click text=Unified The FreightRM >> [placeholder="请输入"]
    page.locator("text=Unified The FreightRM >> [placeholder=\"请输入\"]").click()
    # Fill text=Unified The FreightRM >> [placeholder="请输入"]
    page.locator("text=Unified The FreightRM >> [placeholder=\"请输入\"]").fill("100")
    # Click #location
    page.locator("#location").click()
    # Fill #location
    page.locator("#location").fill("test_point_of_Origin_00001")
    # # Click button:has-text("提 交")
    # page.locator("button:has-text(\"提 交\")").click()
    with page.expect_navigation():
    # Click text=Save and Publish
        page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > form > div.ant-space.ant-space-horizontal.ant-space-align-center > div:nth-child(1) > button").click()
