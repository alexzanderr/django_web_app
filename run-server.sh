#!/usr/bin/sh

# update all deps every time you run
pip freeze > requirements.txt

# make migrations
django_apps=(todos)
for app in $django_apps; do
	python ./manage.py makemigrations $app
done

# migrate everytime you run
python ./manage.py migrate
# run dev server
# this server autoreloads after python code changes
python ./manage.py runserver 5555

