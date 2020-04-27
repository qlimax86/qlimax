FROM balenalib/amd64-python:3
ENTRYPOINT bash
WORKDIR /app
RUN apt-get update && apt-get install -y cron man
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN crontab cronjobs



