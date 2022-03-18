from Admin import product, login
import random

from TestCase.TestAdmin.test_create_product import Random

Random = str(random.randint(0,999))
tran_name = "tran_moudle_000"+Random


def test_1(page):
    login.login(page, username="admin", password="qwer@1234")
    product.create_tran(page,tran_name)
    print(f"Tran Moudle Name : {tran_name}")