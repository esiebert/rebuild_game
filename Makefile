run:
	poetry run black .

lint:
	poetry run isort --check --profile black .
	poetry run black --check .
	poetry run ruff .

format:
	poetry run isort --profile black .
	poetry run black .

test:
	poetry run pytest .
