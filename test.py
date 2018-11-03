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

	b = threading.Thread(target=func.begin, args=(target,))
	t1 = threading.Thread(target=func.readAsk, args=(ref,target,ui.askPrice,spend))
	t2 = threading.Thread(target=func.readBid,args=(ref,target,ui.bidPrice,spend))
	t3 = threading.Thread(target=func.findBuy,args=(target,spend,ui,ellis,fakeOut,fakeRaw))
	#t4 = threading.Thread(target=func.calcProfit,args=(gui,spend,target))
	t5 = threading.Thread(target=func.setMid,args=(target,gui.midPrice))
	#t6 = threading.Thread(target=func.setState,args=(ui,target))
	t7 = threading.Thread(target=func.changeState,args=(target,))
	t8 = threading.Thread(target=func.sell,args=(target,spend,gui,ellis,fakeOut,fakeRaw))

	#configure account value

	r = ref.get(constant.account_url)
	func.setAccount(r.content,ellis,ui)
	print r
	#example buy

	#r = ref.post(constant.preview_url,xml)
	#print r.content


	ellis.fakeCash = func.readFakeCash(fakeRaw)
	#print ellis.fakeCash

	#func.begin(spend)
	#func.sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test","Market is open","nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')

	#func.buildUI(ui)

	#b.start()
	#t6.start()
	#t1.start()
	#t2.start()
	#t7.start()
	#t5.start()
	#t3.start()
	#t4.start()
	#t8.start()


	#ui.top.mainloop()



