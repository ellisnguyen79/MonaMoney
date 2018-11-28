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
spy = info()
opt = option()
ui = gui()
item = spend()
out = "report.txt"
raw = "info.txt"
fakeOut = "fakereport.txt"
fakeRaw = "fakeinfo.txt"
spyReport = ["spyBid.txt","spyAsk.txt","pspyBid.txt","pspyAsk.txt","spyQB.txt","spyQA.txt"]

#data
ref = OAuth1Session(constant.ALLY_CONSUMER_KEY,client_secret=constant.ALLY_CONSUMER_SECRET,resource_owner_key=constant.OAUTH_TOK,resource_owner_secret=constant.OAUTH_TOK_SEC)

xml = """<?xml version="1.0" encoding="UTF-8"?>
<FIXML xmlns="http://www.fixprotocol.org/FIXML-5-0-SP2">
  <Order TmInForce="0" Typ="1" Side="1" Acct="60761352">
    <Instrmt SecTyp="CS" Sym="GE"/>
    <OrdQty Qty="1"/>
  </Order>
</FIXML> """

def run():

	r = ref.get(constant.account_url)
	func.setAccount(r.content,ellis,ui)
	ellis.fakeCash = func.readFakeCash(fakeRaw)
	func.buildUI(ui)
	b.start()
	stream.start()
	update.start()
	#t3.start()
	#t8.start()
	ui.top.mainloop()

#main

if __name__ == "__main__":

	demo = threading.Thread(target=func.tester, args=(target,putTarget))
	update = threading.Thread(target=func.updateUI, args=(spend,target,putTarget,ui))
	b = threading.Thread(target=func.begin, args=(target,putTarget,ref))
	stream = threading.Thread(target=func.read_stream, args=(ui,target,putTarget,spy,spyReport))
	#t1 = threading.Thread(target=func.readAsk, args=(ref,target,ui.askPrice,spend))
	#t2 = threading.Thread(target=func.readBid,args=(ref,target,ui.bidPrice,spend))
	#p1 = threading.Thread(target=func.readPutAsk, args=(ref,putTarget,ui.putaskPrice,spend))
	#p2 = threading.Thread(target=func.readPutBid,args=(ref,putTarget,ui.putbidPrice,spend))
	t3 = threading.Thread(target=func.findBuy,args=(target,putTarget,spend,ui,ellis,fakeOut,fakeRaw))
	#t4 = threading.Thread(target=func.calcProfit,args=(gui,spend,target))
	#t5 = threading.Thread(target=func.setMid,args=(target,gui.midPrice))
	#t6 = threading.Thread(target=func.setState,args=(ui,target))
	#t7 = threading.Thread(target=func.changeState,args=(target,))
	t8 = threading.Thread(target=func.sell,args=(target,spend,gui,ellis,fakeOut,fakeRaw))


	run()

	#r = ref.get(constant.SPY_Quote + "SPY181126C00266500")
	#print r.content






