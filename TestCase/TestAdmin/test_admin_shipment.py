from Admin import login_admin, shipment_admin
from datetime import datetime
import time

admin_username = "admin"
admin_password = "qwer@1234"

module_name_pkg = "Module_"+str(int(time.time()))
first_piece = "1"
freight = "1"
continuation = "1"
rnenw = "1"

def test_create_delivery_pkg(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    module_name=module_name_pkg
    shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
    shipment_admin.SearchDelivery(page, module_name)
    content = page.text_content("text="+module_name)
    assert str(content) != str(module_name)

module_name_weight = "Weight"+str(int(time.time()))
first_weight = "1"
continued_weight = "1"

def test_create_delivery_weight(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    module_name = module_name_weight
    shipment_admin.CreateDeliveryWeight(page, module_name, first_weight, freight, continued_weight, rnenw)
    shipment_admin.SearchDelivery(page, module_name)
    content = page.text_content("text="+module_name)
    assert str(content) != str(module_name)

def test_edit_delivery(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    module_name=module_name_pkg
    shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
    shipment_admin.SearchDelivery(page, module_name)
    module_change_name = "Change_"+module_name
    shipment_admin.EditDelivery(page, module_change_name)
    shipment_admin.SearchDelivery(page, module_change_name)
    content = page.text_content("text="+module_change_name)
    assert str(content) != str(module_change_name)

def test_delete_delivery(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    module_name=module_name_pkg
    shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
    shipment_admin.SearchDelivery(page, module_name)
    shipment_admin.DeleteDelivery(page)
    content = page.text_content(".ant-message-notice-content")
    assert str(content) == "Delete Template Success!"