#!/usr/bin/zsh

app="django_web_app"

if [[ ! -z $APP_FOLDER ]]; then
    cd $APP_FOLDER
fi

cd $app
# durations is to print all durations for every called func
pytest -vv -x -rP -n 2 --color=yes --durations=0