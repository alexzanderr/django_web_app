

# ROOT_NAME = $(notdir $(shell pwd))
# BASENAME_ROOT = $(shell pwd)
# MAIN_BIN = $(ROOT_NAME)
# SPEC_FILE = "$(MAIN_BIN).spec"
# MAIN_FILE = "main.py"

project="django_web_app"

run:
	./run-server.sh

test:
	pytest -vv -x -rP -n 2

lint:
	pylint --load-plugins pylint_django -j 4 `ls -R|grep .py$|xargs`

