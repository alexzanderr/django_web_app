

# ROOT_NAME = $(notdir $(shell pwd))
# BASENAME_ROOT = $(shell pwd)
# MAIN_BIN = $(ROOT_NAME)
# SPEC_FILE = "$(MAIN_BIN).spec"
# MAIN_FILE = "main.py"

project="django_web_app"

run:
	./run-server.sh

dev:
	./run-server.sh

test:
	pytest -vv -x -rP -n 2

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

live:
	python manage.py livereload

ipy:
	python manage.py shell_plus --ptpython

