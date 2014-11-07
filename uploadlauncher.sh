#!/bin/sh

cd /
cd home/pi/sony_qx/
while :
do
	sudo python qx_uploadtoserver.py
done
cd /