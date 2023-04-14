test:
	pytest -s -v tests

.PHONY: lint
lint:
	flake8 --exclude venv  .
	mypy --exclude venv --exclude main .
	black --line-length 79 --skip-string-normalization --check .

.PHONY: test

run:
	uvicorn main:app --reload

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
