PHONY: check
check:
	echo 'Checking...'
	black .
	isort .
	flake8 .