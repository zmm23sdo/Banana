record:
	python3 -m playwright codegen https://admin-banana-test.chunsutech.com/
testA:
	python3 -m pytest -s --headed TestCase/TestAdmin/test_create_product.py
testC:
	python3 -m pytest -s --headed TestCase/TestClient/test_buy.py
debugA:
	PWDEBUG=1 python3 -m pytest -s --headed TestCase/TestAdmin/test_create_product.py
debugC:
	PWDEBUG=1 python3 -m pytest -s --headed TestCase/TestClient/test_buy.py
test:
	python3 -m pytest -s --headed TestCase/test.py
debug:
	PWDEBUG=1 python3 -m pytest -s --headed TestCase/test.py