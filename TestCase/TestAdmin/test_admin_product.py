from Admin import login_admin, product_admin
from datetime import datetime
import time

admin_username = "admin"
admin_password = "qwer@1234"

admin_productname = "Product"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_description = "Product Description:\n\t"+admin_productname+"\n\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_price = "300" 
admin_product_stock = "100" 
admin_product_weight = "1" 
admin_product_freight = "10"

def test_create_product_basic(page): 
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill("productname1234567890")
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click text=productname1234567890
    page.locator("text="+admin_productname).click()    
    content = page.text_content("text="+admin_productname)
    assert content == str(admin_productname)

admin_product_brand = "Brand"+str(int(time.time()))
admin_variation0 = "0Variation"+str(int(time.time()))
admin_option0 = "0option"+str(int(time.time()))
admin_variation1 = "1Variation"+str(int(time.time()))
admin_option3 = "3option"+str(int(time.time()))
admin_product_sku = "sku_"+str(int(time.time()))
admin_product_barcode = "barcode_"+str(int(time.time()))

def test_create_product_advance(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductAdvance(page, admin_productname, admin_product_description, admin_product_brand, admin_variation0,
                         admin_option0, admin_variation1, admin_option3, admin_product_price,
                         admin_product_stock, admin_product_weight, admin_product_sku, admin_product_barcode)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill("productname1234567890")
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click text=productname1234567890
    page.locator("text="+admin_productname).click()    
    content = page.text_content("text="+admin_productname)
    assert content == str(admin_productname)

def test_change_product(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    admin_new_productname =  "Change"+admin_productname
    admin_new_product_description = "Change"+admin_product_description
    product_admin.ChangeProduct(page, admin_productname, admin_new_productname, admin_new_product_description)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_productname)
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click text=productname1234567890
    page.locator("text="+admin_new_productname).click()    
    content = page.text_content("text="+admin_new_productname)
    assert content == str(admin_new_productname)

def test_puton_product(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.PutonProduct(page, admin_productname)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_productname)
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click tbody >> text=Live
    page.locator("td:nth-child(8)").first.click()
    content = page.text_content("td:nth-child(8)")
    # print(f'content:{content}')
    assert content == "Live"

def test_putoff_product(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.PutoffProduct(page, admin_productname)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_productname)
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click tbody >> text=Live
    page.locator("td:nth-child(8)").first.click()
    content = page.text_content("td:nth-child(8)")
    # print(f'content:{content}')
    assert content == "Delisted"

def test_set_productcategory(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.SetProductCategory(page, admin_productname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "设置分组成功!"

def test_set_prduct_freightunified(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.SetProductFreightunified(page, admin_productname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "设置统一运费成功!"

def test_set_product_freighttemplate(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.SetProductFreighttemplate(page, admin_productname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "设置运费模版成功!"