
FROM python:3.6

WORKDIR /django_web_app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 4444
STOPSIGNAL SIGTERM

CMD [ "python", "manage.py", "runserver", "4444"]