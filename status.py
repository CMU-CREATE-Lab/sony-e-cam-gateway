#!/usr/bin/python

import glob, subprocess, os, re, sys, time

os.chdir('/home/pi/sony_qx')

def get_file_size(f):
    try:
        return os.path.getsize(f)
    except:
        return 0

while True:
    downloaded = get_file_size('download-count')
    uploaded = get_file_size('upload-count')
    waiting = len(glob.glob('*_image.jpg'))
    wifi = re.sub(r'\s+', ' ', subprocess.check_output('/sbin/iwconfig wlan0 | egrep "wlan0|Bit Rate|Link Quality"', shell=True).rstrip())
    sys.stderr.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ' | Downloaded:%d | Uploaded:%d | Waiting:%d | Wifi %s\n' % (downloaded, uploaded, waiting, wifi))
    time.sleep(60)
