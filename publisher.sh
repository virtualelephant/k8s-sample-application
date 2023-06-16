#!/bin/sh

# Add cronjob to execute the publisher script every minute
echo "* * * * * python publisher.py >> /var/log/publisher.log 2>&1" > /etc/cron.d/publisher-cron

crontab /etc/cron.d/publisher-cron

foreground
cron -f
