

# ROOT_NAME = $(notdir $(shell pwd))
# BASENAME_ROOT = $(shell pwd)
# MAIN_BIN = $(ROOT_NAME)
# SPEC_FILE = "$(MAIN_BIN).spec"
# MAIN_FILE = "main.py"

project="django_web_app"

dev:
	./run-server.sh

live:
	python manage.py livereload

ipy:
	python manage.py shell_plus --ptpython

run_server:
	./maker run_server

server_plus:
	./maker server_plus

test:
	# durations is to print all durations for every called func
	pytest -vv -x -rP -n 2 --color=yes --durations=0

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
