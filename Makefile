test:
	pytest -s -v tests

.PHONY: test

lint:
	flake8 --exclude venv  .
	black --line-length 79 --skip-string-normalization --check .

.PHONY: lint

run:
	uvicorn main:app --reload

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
