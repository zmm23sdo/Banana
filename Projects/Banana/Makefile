api:
	swagger-codegen generate -i ./client.json -l python -o ./ClientApi
	swagger-codegen generate -i ./services.json -l python -o ./ServicesApi
setup:
	sudo python3 ./AdminApi/setup.py install
	sudo python3 ./ClientApi/setup.py install
	sudo python3 ./ServicesApi/setup.py install
	
PTA: 
	export PYTHONPATH=$$PYTHONPATH:/Users/zhangmingwei/Projects/Banana/AdminApi&&python3 -m pytest -s TestAdmin
PTC:
	export PYTHONPATH=$$PYTHONPATH:/Users/zhangmingwei/Projects/Banana/ClientApi&&python3 -m pytest -s TestClient
PTS:
	export PYTHONPATH=$$PYTHONPATH:/Users/zhangmingwei/Projects/Banana/ServicesApi&&python3 -m pytest -s TestServices
pytest_admin:
	python3 -m pytest -s TestAdmin
pytest_client:
	python3 -m pytest -s TestClient
pytest_services:
	python3 -m pytest -s TestServices


