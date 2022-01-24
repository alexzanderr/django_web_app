

# ROOT_NAME = $(notdir $(shell pwd))
# BASENAME_ROOT = $(shell pwd)
# MAIN_BIN = $(ROOT_NAME)
# SPEC_FILE = "$(MAIN_BIN).spec"
# MAIN_FILE = "main.py"

APP=django_web_app

dev:
	./maker dev

live:
	./maker live

ipy:
	./maker ipy

dev+:
	./maker dev+

test:
	# you cant cd in makefile
	# because cd is a shell function
	# you cant only run commands inside make
	./maker test


lint:
	pylint --load-plugins pylint_django -j 4 `ls -R|grep .py$|xargs`

guni:
	./gunicorn.sh


clean:
	rm -rfv __pycache__
	rm -rfv build
	rm -rfv dist
	rm -rfv $(SPEC_FILE)
	rm -rfv .pytest_cache


mypy:
	mypy --install-types .
