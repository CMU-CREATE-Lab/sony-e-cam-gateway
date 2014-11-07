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

#download 'requests':
#curl -OL https://github.com/kennethreitz/requests/tarball/master
#tar -zxvf master
#cd cd kennethreitz-requests-6b58a35/
#sudo python setup.py install



#payload = {'id': "CREATELabQX10"}
f = open('/media/QX_CONFIG/id.txt','r')
p = '{\'id\': \"'+(f.readline()).strip()+'\"}'
f.close()
payload = ast.literal_eval(p) 

#url = 'http://staging.breathecam.cmucreatelab.org:80/upload'

g = open('/media/QX_CONFIG/server.txt','r')
url = g.readline().strip()
g.close()




print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": starting application"
print "payload: "+str(payload)
print "url: "+url

while True:

    try:
        listOfFiles = glob.glob("*_image.jpg")
        if len(listOfFiles) > 0:
            print "------------------------------------------------------------------------------------------"
            fileToSend = listOfFiles[0]
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Sending image to server ["+fileToSend+"]"
            
            files = {'images[]':open(fileToSend)} #'file' => name of html input field
            r = requests.post(url, data=payload, files=files, timeout = 5)
            response2 = str(r.json)
            if (response2.find("200") > 0):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Got a 200 from server, image upload successful"
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Deleting Image"
                os.remove(fileToSend)
            else:
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Bad response from server, image upload failed"
            
            print "------------------------------------------------------------------------------------------"
        else:
            time.sleep(0.5)

    except:
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:", sys.exc_info()[0]
        print "------------------------------------------------------------------------------------------"
        continue

