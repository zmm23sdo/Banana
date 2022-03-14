import random

def create_order(page,product_name):
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
    # Click text=Exterior
    page.locator("text=Exterior").click()
    # Click text=Wiper
    page.locator("text=Wiper").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill("test_product_description_000"+str(random.randint(0,9999)))
    
    # Click span[role="button"]:has-text("单击上传")
    page.locator("span[role=\"button\"]:has-text(\"单击上传\")").click()
    # Upload 2040336dd894186ef699715bb88a0ecd.jpg
    page.locator("span[role=\"button\"]:has-text(\"单击上传\")").set_input_files("/Users/michaelcheung/Desktop/2040336dd894186ef699715bb88a0ecd.jpg")
    
    
    # Click .ant-select-selection-overflow >> nth=0
    page.locator(".ant-select-selection-overflow").first.click()
    # Click text=Tests分组 A >> span >> nth=1
    page.locator("text=Tests分组 A >> span").nth(1).click()
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
    # Click text=Audi >> nth=1
    page.locator("text=Audi").nth(1).click()
    # Click .ant-select.ant-select-status-success.ant-pro-filed-search-select .ant-select-selector .ant-select-selection-overflow
    page.locator(".ant-select.ant-select-status-success.ant-pro-filed-search-select .ant-select-selector .ant-select-selection-overflow").click()
    # Click .ant-space-item div div:nth-child(4) .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector .ant-select-selection-overflow
    page.locator(".ant-space-item div div:nth-child(4) .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector .ant-select-selection-overflow").click()
    # Click text=宝马X
    page.locator("text=宝马X").click()
    # Click .ant-select.ant-select-status-success.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-focused .ant-select-selector .ant-select-selection-overflow
    page.locator(".ant-select.ant-select-status-success.ant-pro-filed-search-select.pro-field.pro-field-xl.ant-select-focused .ant-select-selector .ant-select-selection-overflow").click()
    # Click text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").click()
    # Click text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").click()
    # Double click text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").dblclick()
    # Fill text=PriceRM >> [placeholder="请输入"]
    page.locator("text=PriceRM >> [placeholder=\"请输入\"]").fill("100")
    # Click #stock
    page.locator("#stock").click()
    # Click .ant-input-affix-wrapper.ant-input-affix-wrapper-focused
    page.locator(".ant-input-affix-wrapper.ant-input-affix-wrapper-focused").click()
    # Fill #stock
    page.locator("#stock").fill("100")
    # Click text=Weightkg >> [placeholder="请输入"]
    page.locator("text=Weightkg >> [placeholder=\"请输入\"]").click()
    # Fill text=Weightkg >> [placeholder="请输入"]
    page.locator("text=Weightkg >> [placeholder=\"请输入\"]").fill("100")
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
    # Click button:has-text("提 交")
    page.locator("button:has-text(\"提 交\")").click()
    
    