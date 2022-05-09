

.PHONY: install
install:
	poetry install

.PHONY: build
build: install
	poetry build

.PHONY: black
black:
	poetry run black .

.PHONY: pytest
pytest:
	poetry run pytest --cov=./tests --black -rAP 


# ALEMBIC COMMANDS

.PHONY: init
init:
	poetry run alembic init demo