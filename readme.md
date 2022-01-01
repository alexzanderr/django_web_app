
# quick info
please `dont read` this `readme`, because i didnt have time to present everything in details

# Just a Django project

quick description about this project:
- python 3.6.15
- django 3.0.1
- git managed project and hosted here on github
- virtual environment for better python version and depedency management
- OOP inheritance
- django templates
- classes as views
- it has an REST API created with django rest framework 3.13.1
- mongo db (NoSQL database)
- postgresql (SQL database)
- django db models
- pytest framework for testing
- it was deployed with gunicorn behind nginx
- docker container (not yet :( )
- it has a register webpage for creating new account with server side validation (users are stored in mongo)
- it has a todo app that uses mongo db
- has template inhertitation ({% extends ... %})
- uses Jquery + ajax
- kubernetes? nah, its too big to implement in 2 days


```py
python manage.py createsuperuser --email just.python.mail.test@gmail.com --username alexzander
```


# Pytest on this project

## test a single file using pytest

testing the entire file `test_management_commands_manage_api.py`
```shell
pytest -vv -x -rP -n 2 api/tests/test_management_commands_manage_api.py
```
args:
- `-vv` is for extra verbose
- `-x` to stop after first fail
- `-rP` for capturin standard output from the test func
- `-n` number of workers (making the tests run in parallel) (you need `pytest-xdist` for this; `pip install pytest-xdist`)

## test a single function using pytest

testing only the function `test_manage_api` from the `test_management_commands_manage_api.py` file
```shell
pytest -vv -x -rP -n 2 api/tests/test_management_commands_manage_api.py::test_manage_api
```

you can use `pytest -k test_manage_api`, but this is not good, because it searches in the entire repo for the function and takes some time

with the previous example pytest `jumps` only to the specified function


# create django project inside venv without creating extra directories
```shell
django-admin startproject $name .
```
note: `.` is very important


# disclaimer
ofcourse there are a lot of quick snippet for solvig problems that i could have pasted here, but i was too lazy for that because i had a deadline, so enjoy a short readme


# Database Migrations

## make migrations only for a specific app
```shell
❱  ./manage.py makemigrations analytics
Migrations for 'analytics':
  analytics/migrations/0002_auto_20211229_1553.py
    - Rename table for todosvisitcount to todos_route_visit_counts
```

## migrate only for a specific app and database
```shell
❱  ./manage.py migrate analytics --database=django_web_app_mysql_db
Operations to perform:
  Apply all migrations: analytics
Running migrations:
  Applying analytics.0002_auto_20211229_1553... OK
```


# Documentation for django
references:
- https://www.quora.com/How-do-you-organize-the-code-in-your-Django-project
- https://www.quora.com/What-are-some-best-practices-for-Django-development
- https://github.com/phpdude/django-template-names
- https://github.com/jpadilla/django-project-template
- https://github.com/vigo/django2-project-template
- https://github.com/skorokithakis/django-project-template
- https://github.com/NUKnightLab/django-project-template
- https://www.toptal.com/django/django-top-10-mistakes
- https://learndjango.com/tutorials/template-structure
- https://stackoverflow.com/questions/54540710/in-django-how-do-you-reference-your-project-urls-py-urls?rq=1
- https://stackoverflow.com/questions/66185424/django-how-do-i-handle-urls-with-multiple-apps
- https://stackoverflow.com/questions/50379634/django-cant-find-template-in-app
- https://djangostars.com/blog/django-pytest-testing/
- https://www.djangoproject.com/start/
- https://stackoverflow.com/questions/41926032/django-load-static-files-from-another-app
- https://www.digitalocean.com/community/tutorials/working-with-django-templates-static-files
- https://stackoverflow.com/questions/1208067/wheres-my-json-data-in-my-incoming-django-request/3244765#3244765
- https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django
- https://github.com/jazzband/django-redis
- https://docs.djangoproject.com/en/4.0/topics/db/multi-db/
- https://dev.to/minhvuong1/how-to-set-up-multiple-databases-on-django-1c76
- https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/
- https://stackoverflow.com/a/22557095/12172291
- https://docs.djangoproject.com/en/4.0/topics/testing/tools/
- https://stackoverflow.com/questions/1579846/django-returning-http-301
- https://stackoverflow.com/questions/31335736/cannot-apply-djangomodelpermissions-on-a-view-that-does-not-have-queryset-prot
- https://stackoverflow.com/questions/68024060/assertionerror-database-connection-isnt-set-to-utc
- https://stackoverflow.com/questions/5500472/how-do-i-match-the-question-mark-character-in-a-django-url
- https://github.com/stephenmcd/django-socketio
- https://stackoverflow.com/questions/20175243/django-gunicorn-not-load-static-files
- https://docs.docker.com/samples/django/
-
- https://code.djangoproject.com/wiki/DjangoAndPyPy
- https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
- https://stackoverflow.com/questions/20175243/django-gunicorn-not-load-static-files
- https://stackoverflow.com/questions/1474374/nginx-doesnt-serve-static
- https://stackoverflow.com/questions/1275486/django-how-can-i-see-a-list-of-urlpatterns
- https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
- https://github.com/realpython/dockerizing-django
- https://www.youtube.com/watch?v=vJAfq6Ku4cI
- https://github.com/stephenmcd/django-socketio
- https://github.com/jazzband/django-redis
- https://stackoverflow.com/questions/1275486/django-how-can-i-see-a-list-of-urlpatterns
- https://realpython.com/django-nginx-gunicorn/
- https://github.com/dcramer/django-devserver
- https://docs.djangoproject.com/en/3.1/intro/reusable-apps/
- https://docs.djangoproject.com/en/4.0/topics/db/multi-db/
- https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
- https://www.django-rest-framework.org/api-guide/authentication/
- https://dzone.com/articles/cookies-vs-tokens-the-definitive-guide
- https://stackoverflow.com/questions/3519143/django-how-to-specify-a-database-for-a-model/60453322#60453322
- https://stackoverflow.com/questions/3519143/django-how-to-specify-a-database-for-a-model
- https://stackabuse.com/building-a-graphql-api-with-django/
- https://stackabuse.com/working-with-redis-in-python-with-django/
- https://www.youtube.com/watch?v=b-6mEAr1m-A
- https://stackoverflow.com/questions/70185942/why-i-am-getting-not-implemented-error-database-objects-do-not-implement-truth
- https://django-mongodb-engine.readthedocs.io/en/latest/tutorial.html#migration-free-model-changes
- https://www.willmcgugan.com/blog/tech/post/richer-django-logging/
- https://stackoverflow.com/questions/23832375/how-to-set-up-a-custom-logger-filter-in-django
- https://www.youtube.com/watch?v=4zbehnz-8QU (de pus minutul 9 in django exceptions)
- https://stackoverflow.com/questions/17066074/modelserializer-using-model-property
- https://testdriven.io/blog/django-stripe-tutorial/
- https://stackoverflow.com/questions/26080303/improperlyconfigured-settings-databases-is-improperly-configured-please-supply
- https://sydjameer.medium.com/how-to-expose-your-multiple-database-for-admin-site-in-django-50a7870d14ab
- https://stackoverflow.com/questions/27573358/how-to-get-pytest-django-to-only-run-tests-for-a-single-app
- https://django-configurations.readthedocs.io/en/stable/
- https://github.com/phpdude/docker-django-webpack-skeleton
- https://stackoverflow.com/questions/4096863/how-to-get-and-set-the-current-web-page-scroll-position
- https://www.sipios.com/blog-tech/monitoring
-
-
-
