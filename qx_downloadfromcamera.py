#!/usr/bin/python

from datetime import datetime
from urllib import urlretrieve
from time import gmtime, strftime, mktime
import os
import time
import socket
import httplib
import sys

ip = "10.0.0.1"
port = 10000

print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": starting application"

downloadCount = open('download-count', 'a')

while True:

    curDate = str(int(time.mktime(datetime.utcnow().timetuple())))

    try:
        sys.stderr.write("******************************************************************************************\n")
        sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": taking picture\n")
        httpServ = httplib.HTTPConnection(ip, port, timeout=5)
        httpServ.connect()
        httpServ.request('POST', '/sony/camera', '{\"method\":\"actTakePicture\",\"params\":[],\"id\":10,\"version\":\"1.0\"}')
        response = httpServ.getresponse()
        
        if response.status == httplib.OK:
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": picture taken, beginning download\n")
            resp = response.read()
            respSplit = resp.split('\"');
            imageName = curDate+'_img'+'.jpg'
            imageDoneName = curDate+'_image'+'.jpg'
            urlretrieve(respSplit[5], imageName)
            
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": picture saved ["+imageName+"]\n")
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": picture renamed ["+imageDoneName+"]\n")
            os.rename(imageName,imageDoneName)
            downloadCount.write('+')
            downloadCount.flush()
        else:
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": bad request\n")
        
        httpServ.close()
        sys.stderr.write("******************************************************************************************\n")

    except:
        error = str(sys.exc_info()[0])
        if error.find("socket") > 0:
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Error: Cannot talk to camera\n")
        else:
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:"+ error + "\n")
        sys.stderr.write("******************************************************************************************\n")
        continue

