############################################################################
# Dockerfile to run a cron job
# Based on Ubuntu
############################################################################

# set the base image to Ubuntu
FROM ubuntu:latest

# create a new folder inside the container
RUN mkdir -p /app

# copy all the files in local machine  inside the container
COPY . /app

# install Python and basic Python tools
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip 

# install crontab
RUN apt-get install -y cron

# get pip to download and install requirements
RUN pip3 install -r /app/requirements.txt

# copy the local crontab file to new location
RUN cp /app/myCron2 /etc/cron.d/hello-cron

# create a log file
RUN touch /var/log/cron.log

# make the crontab file executable
RUN chmod +x /etc/cron.d/hello-cron

# run the crontab job 
RUN crontab /etc/cron.d/hello-cron
CMD cron && tail -f /var/log/cron.log
