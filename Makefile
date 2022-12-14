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
PWadmin:
	python3 -m playwright codegen https://admin-banana-dev.chunsutech.com/
PWclient:
	python3 -m playwright codegen https://client-banana-dev.chunsutech.com/
proxy:
	git config --global http.proxy socks5://127.0.0.1:1080
	git config --global http.https://github.com.proxy socks5://127.0.0.1:1080
