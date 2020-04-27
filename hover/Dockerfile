FROM balenalib/amd64-debian-python:3
WORKDIR /app
RUN apt-get update && apt-get install -y cron
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN crontab cronjobs
RUN chmod 0744 start.sh
