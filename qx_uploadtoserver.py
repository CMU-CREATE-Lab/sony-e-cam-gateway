#!/usr/bin/python

from datetime import datetime
from urllib import urlretrieve
from time import gmtime, strftime, mktime
import os
import time
import socket
import httplib
import requests
import glob
import sys
import ast

uploadCount = open('upload-count', 'a')

payload = {'id': "CREATELabQX10"}

url = 'http://staging.breathecam.cmucreatelab.org:80/upload'

sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": starting application\n")
sys.stderr.write("payload: "+str(payload)+"\n")
sys.stderr.write("url: "+url+"\n")

while True:
    try:
        listOfFiles = sorted(glob.glob("*_image.jpg"))
        if len(listOfFiles) > 0:
            sys.stderr.write("------------------------------------------------------------------------------------------\n")
            fileToSend = listOfFiles[0]
            sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Sending image to server ["+fileToSend+"]\n")
            
            files = {'images[]':open(fileToSend)} #'file' => name of html input field
            r = requests.post(url, data=payload, files=files, timeout = 5)
            response2 = str(r.json)
            if (response2.find("200") > 0):
                sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Got a 200 from server, image upload successful\n")
                sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Deleting Image\n")
                os.remove(fileToSend)
                uploadCount.write('+')
                uploadCount.flush()
            else:
                sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Bad response from server, image upload failed\n")
            
            sys.stderr.write("------------------------------------------------------------------------------------------\n")
        else:
            time.sleep(0.5)

    except:
        sys.stderr.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:", sys.exc_info()[0]+"\n")
        sys.stderr.write("------------------------------------------------------------------------------------------\n")
        continue

