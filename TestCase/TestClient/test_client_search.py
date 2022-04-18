from Admin import login_admin, product_admin
from Client import login_client, search_client, buy_client
import datetime


admin_username = "admin"
admin_password = "qwer@1234"

admin_productname = "Product"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_description = "Product Description:\n\t"+admin_productname+"\n\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_price = "300" 
admin_product_stock = "100" 
admin_product_weight = "1" 
admin_product_freight = "10"

customer_phone = "8615195927818"
customer_password = "qwer`123"

def test_search_product(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    search_client.SearchProduct(page, admin_productname)
    page.locator("text="+admin_productname).hover()
    content = page.text_content("text="+admin_productname)
    assert content == str(admin_productname)