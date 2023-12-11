VENV := .venv

PYTHON := poetry run python
TOUCH := $(PYTHON) -c 'import sys; from pathlib import Path; Path(sys.argv[1]).touch()'

poetry.lock: pyproject.toml
	poetry lock

# Build venv with Python deps.
$(VENV):
	@echo Installing Poetry environment
	@poetry install
	@$(TOUCH) $@

# Convenience target to build venv
.PHONY: setup
setup: $(VENV)

.PHONY: check
check: $(VENV)
	@echo Checking Poetry lock: Running poetry lock --check
	@poetry lock --check
	@echo Linting code: Running pre-commit
	@poetry run pre-commit run -a
	@echo Type checking code: Running mypy
	@MYPYPATH=stubs poetry run mypy adventofcode

.PHONY: test
test: $(VENV)
	@echo Testing code: Running pytest
	@poetry run coverage run -p -m pytest

.PHONY: coverage
coverage: $(VENV)
	@echo Testing covarage: Running coverage
	@poetry run coverage combine
	@poetry run coverage html --skip-covered --skip-empty
	@poetry run coverage report

.PHONY: build
build:
	@echo Creating wheel file
	@poetry build

.PHONY: clean
clean:
	@echo Cleaning ignored files
	@git clean -Xfd

.DEFAULT_GOAL := test
