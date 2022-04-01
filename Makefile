.PHONY: clear run  install-deps

install-deps:
	pip install -r requirements.txt

clear:
	rm -rf dist

run:
	python3 ./scanner/scanner.py

.DEFAULT_GOAL := run