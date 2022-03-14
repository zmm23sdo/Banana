record:
	python3 -m playwright codegen https://admin-banana-test.chunsutech.com/
test:
	python3 -m pytest -s --headed TestCase/test_create_product.py