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
	python -m etl.main

linter:
	pylint etl --fail-under=7

launch_metabase:
	docker run -v $(PWD):/metabase -d -p 3000:3000 --name metabase metabase/metabase
