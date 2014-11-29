#!/bin/sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /home/pi/sony_qx/
while :
do
    python qx_downloadfromcamera.py  >> /home/pi/sony_qx/logs/download.log 2>&1
done
