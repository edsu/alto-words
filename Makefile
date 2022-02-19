VENV := ./.venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python

.PHONY: help
help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Create a virtual environment
	python3 -m venv .venv

.PHONY: install
install: venv ## Install dependencies in virtual environment
	$(VENV)/bin/pip install -r requirements.txt

enwiktionary-latest-page.sql.gz:
	echo 'Downloading dewiktionary-latest-page.sql.gz'
	curl http://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-page.sql.gz -o enwiktionary-latest-page.sql.gz

dictionary.db: enwiktionary-latest-page.sql.gz ## Create dictionary for English
	echo 'Creating the dictionary file'
	$(PYTHON) make_dictionary.py enwiktionary-latest-page.sql.gz

.PHONY: clean
clean: dictionary.db ## Remove the dictionary file
	rm -rf dictionary.db
