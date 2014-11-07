#!/bin/sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/sony_qx/
while :
do
	sudo python qx_downloadfromcamera.py
done
cd /