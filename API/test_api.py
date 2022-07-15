from TestInterface import Interface
import time
import datetime
import random
import unicodedata

inter = Interface()

test_datetime =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
test_time = str(time.time())
test_random = str(random.randint(0,999))

# def test_admin_login():
#     test_admin_login = inter.admin_login(
#         username = "mvtest1",
#         password = "qwer`123",
#         headers = {'Content-Type':'application/json', 'X-Tenant-Type':'admin'}
#     )
#     print('\n','='*100)
#     # print('test_admin_login:',test_admin_login.json())
#     token = str(test_admin_login.json()['access'])
#     print(f'Token:',{token})

def test_admin_product():
    admin_login = inter.admin_login(
        username = "mvtest1",
        password = "qwer`123",
        headers = {'X-Tenant-Type':'admin'}
    )
    print(f'\n'+"="*100)
    # print('test_admin_login:',test_admin_login.json())
    token = str(admin_login.json()['access'])
    print(f'Token:',{token})
    print('='*100)

    test_admin_product = inter.admin_product(
        name = "Product" + test_datetime, 
        category_id = "13", 
        brand_id = "", 
        describe = "Product" + test_time + "\n" + test_datetime, 
        pic_name1 = "1图片.jpeg", 
        pic_media_type1 = "1", 
        pic_url1 = "https://buybye-oss-dev.chunsutech.com/banana/media/2ce20da1e2be4596a1c1eef5bc9612f7",
        pic_name2 = "2图片.jpeg", 
        pic_media_type2 = "1", 
        pic_url2 = "https://buybye-oss-dev.chunsutech.com/banana/media/0a26ff82439646ccbb3b40ff7df09297",
        pic_name3 = "3图片.jpeg", 
        pic_media_type3 = "1", 
        pic_url3 = "https://buybye-oss-dev.chunsutech.com/banana/media/3fe4db6aeb8e4f3a93d731a7fb180dda",
        pic_name4 = "4图片.jpeg", 
        pic_media_type4 = "1", 
        pic_url4 = "https://buybye-oss-dev.chunsutech.com/banana/media/e56751c3b834437da0dda0e50168a6b4",
        pic_name5 = "5图片.jpeg", 
        pic_media_type5 = "1", 
        pic_url5 = "https://buybye-oss-dev.chunsutech.com/banana/media/490f8ed9ed3045d2981bb1941f788c1c",
        pic_name6 = "6图片.jpeg", 
        pic_media_type6 = "1", 
        pic_url6 = "https://buybye-oss-dev.chunsutech.com/banana/media/1361c924124743b5b80c937198846265",
        pic_name7 = "7图片.jpeg", 
        pic_media_type7 = "1", 
        pic_url7 = "https://buybye-oss-dev.chunsutech.com/banana/media/019b8181dd8c4c18b0ac4dc5d967afec",
        pic_name8 = "8图片.jpeg", 
        pic_media_type8 = "1", 
        pic_url8 = "https://buybye-oss-dev.chunsutech.com/banana/media/a8af36d72f034979b2dc89a04e3fa473",
        pic_name9 = "9图片.jpeg", 
        pic_media_type9 = "1",
        pic_url9 = "https://buybye-oss-dev.chunsutech.com/banana/media/8ce514f9933a46b2a0cc27007510d577",
        pic_name10 = "10图片.jpeg", 
        pic_media_type10 = "1" , 
        pic_url10 = "https://buybye-oss-dev.chunsutech.com/banana/media/1e62aef12cae413181443fbd197a58bc",
        group_id = "22", 
        brand = "Brand"+test_time, 
        warranty_duration = "12 Months", 
        warranty_type = "Supplier Warranty", 
        price = "300.00", 
        stock = "100", 
        weight = "1.00", 
        barcode = "Bar"+test_time+"Code", 
        admin_sku = "Sku"+test_time,
        uid1 = "UidA"+test_time, 
        url1 = "https://buybye-oss-dev.chunsutech.com/banana/media/67fff4f4e134414890c3f32a6c152dc3", 
        name1 = "240图片.jpeg", 
        media_type1 = "1", 
        vid1 = "VidA"+test_time, 
        oid1 = "OidA"+test_time,
        sys_sku1 = "System"+test_time+"skuA"+test_random,
        Variation1key = "A", 
        Variation1val1 = "1-1", 
        Variation2key = "B",
        Variation2val1 = "2-1", 
        Variation3key = "C", 
        Variation2val2 = "2-2",
        Variation2val3 = "2-3", 
        Variation2val4 = "2-4", 
        Variation2val5 = "2-5",
        uid2 = "UidB"+test_time, 
        url2 = "https://buybye-oss-dev.chunsutech.com/banana/media/3a2a99926af042c099a1e8acff3a3cc4", 
        name2 = "241图片.jpeg", 
        oid2 = "OidB"+test_time, 
        Variation1val2 = "1-2",
        uid3 = "UidC"+test_time, 
        url3 = "https://buybye-oss-dev.chunsutech.com/banana/media/eda107baf72d42d795600ffc33867014", 
        name3 = "242图片.jpeg", 
        oid3 = "OidC"+test_time, 
        Variation1val3 = "1-3",
        uid4 = "UidE"+test_time, 
        url4 = "https://buybye-oss-dev.chunsutech.com/banana/media/0767f408bfea4d07b49dc987e467fa77", 
        name4 = "243图片.jpeg", 
        oid4 = "OidE"+test_time, 
        Variation1val4 = "1-4",
        uid5 = "UidF"+test_time, 
        url5 = "https://buybye-oss-dev.chunsutech.com/banana/media/1af066bf09f54ea6805be0c77c418f24", 
        name5 = "244图片.jpeg", 
        oid5 = "OidF"+test_time, 
        Variation1val5 = "1-5",
        is_publish = True, 
        trans_price = "300", 
        template_id = "0", 
        location = "Sarawak",
        location_id = "", 
        parent_brand_id = "1", 
        spu = "SPU"+test_time,
        headers = {'Authorization': token, 'X-Tenant-Type':'admin'}
    )
    print(f'\n'+"="*100)
    print(f'test_admin_product:',{test_admin_product.status_code})
    print('test_admin_product:',test_admin_product.json())
    print(f"="*100)
    assert str(test_admin_product.status_code) == '200'
    