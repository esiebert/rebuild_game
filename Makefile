run:
	poetry run python3 rebuild_game

install:
	poetry install

lint:
	poetry run isort --check --profile black .
	poetry run black --check .
	poetry run ruff .

format:
	poetry run isort --profile black .
	poetry run black .

test:
	poetry run pytest .
