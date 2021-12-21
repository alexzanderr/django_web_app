
FROM python:3.6

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
# every ouput and every error will pe printed to stdout (shell output)
ENV PYTHONUNBUFFERED=1



WORKDIR /django_web_app
COPY requirements.txt /django_web_app/
RUN pip install -r requirements.txt

COPY . /django_web_app/

# EXPOSE 4444
# STOPSIGNAL SIGTERM


# 0.0.0.0 will run on every interface
# CMD [ "python", "manage.py", "runserver", "localhost:4444"]