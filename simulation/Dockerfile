
FROM python:3.6

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
# every ouput and every error will pe printed to stdout (shell output)
ENV PYTHONUNBUFFERED=1



# creates the directory if it doesnt exist
WORKDIR /django_web_app_simulation
COPY requirements.txt /django_web_app_simulation/
RUN pip install -r requirements.txt

COPY . /django_web_app_simulation/
