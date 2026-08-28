POETRY ?= poetry run

.DEFAULT_GOAL := help
.PHONY: help install stage serve build clean

help:  ## List the available targets
	@grep -hE '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies from poetry.lock
	poetry install

stage:  ## Rebuild build/docs from docs/ (re-run after editing while serving)
	$(POETRY) python tools/prepare.py

serve:  ## Stage the docs and start the dev server
	$(POETRY) python tools/prepare.py
	$(POETRY) zensical serve

build:  ## Full strict build, exactly as CI runs it
	$(POETRY) python tools/prepare.py --strict
	$(POETRY) zensical build --strict
	$(POETRY) python tools/permalinks.py --strict

clean:  ## Remove the staged docs and the built site
	rm -rf build site
