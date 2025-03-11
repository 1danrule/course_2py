PHONY: test
test:
	@echo 'Testing started...'
	@pytest . -v


PHONY: check
check: test
	@echo 'Checking started...'
	black .
	isort .
	flake8 .