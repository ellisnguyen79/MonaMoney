import xml.etree.ElementTree as ET
import requests
import json
import time
import threading 
import time

import sys
sys.path.insert(0, '../')
import constant
import func

from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1

from classes import *
from Tkinter import *

#class
ellis = User()
target = info()
putTarget = info()
opt = option()
ui = gui()
item = spend()
out = "report.txt"
raw = "info.txt"
fakeOut = "fakereport.txt"
fakeRaw = "fakeinfo.txt"

#data
ref = OAuth1Session(constant.ALLY_CONSUMER_KEY,client_secret=constant.ALLY_CONSUMER_SECRET,resource_owner_key=constant.OAUTH_TOK,resource_owner_secret=constant.OAUTH_TOK_SEC)

xml = """<?xml version="1.0" encoding="UTF-8"?>
<FIXML xmlns="http://www.fixprotocol.org/FIXML-5-0-SP2">
  <Order TmInForce="0" Typ="1" Side="1" Acct="60761352">
    <Instrmt SecTyp="CS" Sym="GE"/>
    <OrdQty Qty="1"/>
  </Order>
</FIXML> """

#main

if __name__ == "__main__":

	print "Seq"

	


