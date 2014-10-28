#!/usr/bin/python3
#Full list of commands
#http://developer.lgappstv.com/TV_HELP/index.jsp?topic=%2Flge.tvsdk.references.book%2Fhtml%2FUDAP%2FUDAP%2FAnnex+A+Table+of+virtual+key+codes+on+remote+Controller.htm
import http.client
from tkinter import *
import xml.etree.ElementTree as etree
import socket
import re
import sys
import time
lgtv = {}
dialogMsg =""
headers = {"Content-Type": "application/atom+xml"}
lgtv["pairingKey"] = sys.argv[3]
def getip():
    ipaddress = sys.argv[2]
    return ipaddress
def displayKey():
    conn = http.client.HTTPConnection( lgtv["ipaddress"], port=8080)
    reqKey = "<!--?xml version=\"1.0\" encoding=\"utf-8\"?--><auth><type>AuthKeyReq</type></auth>"
    conn.request("POST", "/roap/api/auth", reqKey, headers=headers)
    httpResponse = conn.getresponse()
    if httpResponse.reason != "OK" : sys.exit("Network error")
    return httpResponse.reason
def getSessionid():
    conn = http.client.HTTPConnection( lgtv["ipaddress"], port=8080)
    pairCmd = "<!--?xml version=\"1.0\" encoding=\"utf-8\"?--><auth><type>AuthReq</type><value>" \
            + lgtv["pairingKey"] + "</value></auth>"
    conn.request("POST", "/roap/api/auth", pairCmd, headers=headers)
    httpResponse = conn.getresponse()
    if httpResponse.reason != "OK" : return httpResponse.reason
    tree = etree.XML(httpResponse.read())
    return tree.find('session').text
def getPairingKey():
    displayKey()
def handleCommand(cmdcode):
    conn = http.client.HTTPConnection( lgtv["ipaddress"], port=8080)
    conn = http.client.HTTPConnection( lgtv["ipaddress"], port=8080)
    cmdText = "<?xml version=\"1.0\" encoding=\"utf-8\"?><command>" \
    +"<name>HandleKeyInput</name><value>" \
    +cmdcode \
    +"</value></command>"
    conn.request("POST", "/roap/api/command", cmdText, headers=headers)
    httpResponse = conn.getresponse()
    return 0
#main()
lgtv["ipaddress"] = getip()
theSessionid = getSessionid()
if theSessionid == "Unauthorized" :
    getPairingKey()
    time.sleep(20)
else:
    theSessionid = getSessionid()
if len(theSessionid) < 8 : sys.exit("Could not get Session Id: " + theSessionid)
lgtv["session"] = theSessionid
#displayKey()
result = str(sys.argv[1])
handleCommand(result)
