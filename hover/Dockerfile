FROM python:3-stretch
RUN mkdir -p /app/hover/
COPY * /app/hover/
COPY cronjobs /etc/cron.d/
RUN chmod 0644 /etc/cron.d/cronjobs
RUN touch /var/log/cron.log
RUN apt-get update && apt-get -y install cron
RUN pip install -r /app/hover/requirements.txt
# CMD cron && tail -f /var/log/cron.log
#CMD ["python", "/app/hover/update_ip.py"]

