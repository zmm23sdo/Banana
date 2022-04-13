from Admin import login_admin, product_admin
from datetime import datetime

admin_username = "admin"
admin_password = "qwer@1234"

admin_prouctname = "Product"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_description = "Product Description:\n\t"+admin_prouctname+"\n\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_price = "300" 
admin_product_stock = "100" 
admin_product_weight = "1" 
admin_product_freight = "10"

def test_create_product_basics(page): 
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_prouctname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    # Go to https://admin-banana-dev.chunsutech.com/commodity/list
    page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill("productname1234567890")
    # Click text=CreateAdvanced Search >> button >> nth=1
    page.locator("text=CreateAdvanced Search >> button").nth(1).click()
    # Click text=productname1234567890
    page.locator("text="+admin_prouctname).click()    
    content = page.text_content("text="+admin_prouctname)
    assert content == str(admin_prouctname)

