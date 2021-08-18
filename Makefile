INPUT_DB='db.db'
INPUT_TABLE='premium_payments'

clean:
	rm -Rf *.egg-info
	rm -Rf build
	rm -Rf dist
	rm -Rf .pytest_cache
	rm -f .coverage

build: clean
	python3 setup.py sdist

install: build
	pip3 install -r requirements.txt
	python setup.py install

run: build
	python -m etl_premium_clients.main
	#--input_db $(INPUT_DB) \
	#--input_table $(INPUT_TABLE)

linter:
	pylint etl_premium_clients --fail-under=7

tests:
	pytest -vv -s
