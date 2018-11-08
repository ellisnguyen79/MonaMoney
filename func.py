import time
import datetime
import smtplib
import requests
from requests_oauthlib import OAuth1
import xml.etree.ElementTree as ET
import sys
sys.path.insert(0, '../')
import constant
import math

def tester(target,putTarget):
	while(1):
		time.sleep(1)
		print "bidCAll: ",target.bid
		print "askCAll: ",target.ask
		print "bidPut: ",putTarget.bid
		print "askPut: ",putTarget.ask

def buildUI(ui):
	ui.top.geometry("600x500")
	ui.acountLabel.place(x=125,y=0,width=130,height=25)
	ui.accountPrice.place(x=255,y=0,width=150,height=25)

	ui.askLabel.place(x=80,y=80,width=50,height=25)
	ui.askPrice.place(x=130,y=80,width=50,height=25)
	ui.bidLabel.place(x=80,y=105,width=50,height=25)
	ui.bidPrice.place(x=130,y=105,width=50,height=25)
	ui.midLabel.place(x=80,y=130,width=50,height=25)
	ui.midPrice.place(x=130,y=130,width=50,height=25)

	#put 
	ui.putaskLabel.place(x=330,y=80,width=50,height=25)
	ui.putaskPrice.place(x=380,y=80,width=50,height=25)
	ui.putbidLabel.place(x=330,y=105,width=50,height=25)
	ui.putbidPrice.place(x=380,y=105,width=50,height=25)
	ui.putmidLabel.place(x=330,y=130,width=50,height=25)
	ui.putmidPrice.place(x=380,y=130,width=50,height=25)


	ui.holdLabel.place(x=80,y=185,width=50,height=25)
	ui.holdPrice.place(x=130,y=185,width=50,height=25)
	ui.profitLabel.place(x=80,y=240,width=50,height=25)
	ui.profitPrice.place(x=130,y=240,width=100,height=25)
	ui.curLabel.place(x=190,y=185,width=50,height=25)
	ui.curPrice.place(x=240,y=185,width=50,height=25)

	#put 
	ui.putholdLabel.place(x=330,y=185,width=50,height=25)
	ui.putholdPrice.place(x=380,y=185,width=50,height=25)
	ui.putprofitLabel.place(x=330,y=240,width=50,height=25)
	ui.putprofitPrice.place(x=380,y=240,width=100,height=25)
	ui.putcurLabel.place(x=440,y=185,width=50,height=25)
	ui.putcurPrice.place(x=490,y=185,width=50,height=25)

def readIn(opt):
	print "enter date: "
	opt.date = raw_input()
	print "enter month: "
	opt.month = raw_input()
	print "CAll?: "
	opt.call = raw_input()
	print "enter strike"
	opt.strike = raw_input()
	opt.symbol = opt.tick + opt.year + opt.month + opt.date + opt.call + "00" + opt.strike + "0"
	print "Genarted symbol: " + opt.symbol

def sendemail(fr,to,cc,sub,msg,login,pas,smtpserver='smtp.gmail.com:587'):
	header = 'From: %s\n' % fr
	header += 'To: %s\n' % ','.join(to)
	header += 'Cc: %s\n' % ','.join(cc)
	header += 'Subject: %s\n\n'% sub

	msg = header + msg

	ser = smtplib.SMTP(smtpserver)
	ser.starttls()
	ser.login(login,pas)
	problem = ser.sendmail(fr,to,msg)
	ser.quit()
	return problem

def begin(target,putTarget,ref):
	print "Running begin()"
	while(1):
		if target.state == 0 or target.state == 1 or target.state == 2:
			print "begin is Sleeping..."
			time.sleep(80)
		time.sleep(1)
		print "Inside begin()"
		week = datetime.datetime.today().weekday()
		hour = datetime.datetime.now().hour
		sec = datetime.datetime.now().second
		if target.state == -2:
			if hour > 14:
				target.state = -1
				putTarget.state = -1
		if target.state == -1:
			#if week < 5 and hour > 6 and hour < 13:
			if(1):
				result = findNewOption(ref)
				target.name = result[1]
				putTarget.name = result[0]
				print target.name
				print putTarget.name 
				#sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test","Market is open","nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')
				target.state = 0
				putTarget.state = 0
			else:
				time.sleep(10)
				print "Not in Market"

def findNewOption(ref):
	plist = []
	rlist = []
	putlist = []
	calllist = []
	stockPrice = 0.0
	qPut = ""
	qCAll = ""
	print "In findNewOption()"
	s = ref.get(constant.spy_url)
	r = ref.get(constant.strike_url)
	p = ref.get(constant.expire_url)
	#print s,r,p
	root = ET.fromstring(r.content)
	poot = ET.fromstring(p.content)
	soot = ET.fromstring(s.content)
	#print root,poot,soot
	for c in soot.iter('last'):
		stockPrice = float(c.text)
	for c in root.iter('price'):
		if float(c.text) < stockPrice + 4 and float(c.text) > stockPrice - 4:
			rlist.append(c.text)
	for c in poot.iter('date'):
		plist.append(c.text)
	
	#print rlist
	#print plist

	d = plist[0].split("-")
	m = list(d[0])
	m[0] = m[2]
	m[1] = m[3]
	m[2] = ""
	m[3] = ""
	mo = "".join(m)
	d[0] = mo

	for i in rlist:
		if len(i) == 3:
			calllist.append("SPY" + d[0] + d[1] + d[2] + "C" + "00" + i + "000")
			putlist.append("SPY" + d[0] + d[1] + d[2] + "P" + "00" + i + "000")
		if len(i) == 5:
			l = list(i)
			l[3] = l[4]
			l[4] = "0"
			r = "".join(l)
			calllist.append("SPY" + d[0] + d[1] + d[2] + "C" + "00" + r + "0")
			putlist.append("SPY" + d[0] + d[1] + d[2] + "P" + "00" + r + "0")
	
	#print calllist
	#print putlist

	putlist.reverse()

	for i in range(len(calllist)):
		q = ref.get(constant.SPY_Quote+calllist[i])
		#print constant.SPY_Quote+calllist[0]
		qoot = ET.fromstring(q.content)
		for c in qoot.iter("ask"):
			if float(c.text) < 1 and qCAll == "":
				qCAll = calllist[i]

	for i in range(len(putlist)):
		q = ref.get(constant.SPY_Quote+putlist[i])
		#print constant.SPY_Quote+calllist[0]
		qoot = ET.fromstring(q.content)
		for c in qoot.iter("ask"):
			if float(c.text) < 1 and qPut == "":
				qPut = putlist[i]


	info = qPut,qCAll
	#print info
	return info

def setBuy(spend,ui):
	ui.holdPrice.config( text=str(spend.hold))
	ui.top.update()

def updateUI(spend,target,putTarget,gui):

	while(1):
		gui.askPrice.config(text=str(target.ask))
		gui.bidPrice.config(text=str(target.bid))
		gui.midPrice.config(text=str(target.mid))
		gui.putaskPrice.config(text=str(putTarget.ask))
		gui.putbidPrice.config(text=str(putTarget.bid))
		gui.putmidPrice.config(text=str(putTarget.mid))
		gui.top.update()
		if target.mid != 0.0 and putTarget.mid != 0.0 and target.state == 0:
			target.state = 1
			gui.curPrice.config(text=str(target.state))
			gui.top.update()
		if target.state == 2:
			gui.profitPrice.config( text=str(round(spend.profit,2)))
			gui.top.update()

def changeState(target):
	while(1):
		time.sleep(0.1)
		if target.state == 0:
			#print "changeState "
			if target.bid != 0.0 and target.ask != 0.0:
				target.state = 1
		else:
			return

def setState(gui,target):
	
	while(1):
		if target.state != 4:
			time.sleep(1)
			print "setState "
			gui.curPrice.config(text=str(target.state))

def setMid(target, midPrice):
	while(1):
		time.sleep(1)
		if target.state == 1:
			print "In setMid: "
			target.mid = round((target.ask + target.bid)/2,2)
			midPrice.config( text=str(target.mid))
			target.state = 2 
		if target.state == 2:
			return

def setSize(spend,ellis):
	spend.size = math.floor(ellis.fakeCash / (spend.hold * 100) ) 
	#print "Quantity size: ", spend.size

def look(target,putTarget,spend):
	Cresist = [0.0,0.0,0.0]
	Csupport = [11110.0,111110.0,111110.0]
	Presist = [0.0,0.0,0.0]
	Psupport = [0.0,0.0,0.0]
	temp = 0.0
	prev = 0.0
	di = {}
	su = {}
	re = {}

	while(spend.hold == 0.0):
		temp = target.ask	
		if temp != prev:
			if target.ask in di:
				di[target.ask] += 1
			else:
				di[target.ask] = 0
	
		if temp > prev:
			if target.ask in di:
				su[target.ask] += 1
			else:
				su[target.ask] = 0
		else:
			if target.ask in di:
				re[target.ask] += 1
			else:
				re[target.ask] = 0
		prev = target.ask
		print "Histogram\n",di,"Support\n",su,"Resist\n",re

def findBuy(target,spend,gui,ellis,out,raw):
	while(1):
		if target.state == 1:	

			# DETERMINE

			look(target,putTarget,spend)

			####


			setSize(spend,ellis)
			#print "we bought this price: " , spend.hold
			setBuy(spend,gui)
			target.msg = "Quantity: " + str(spend.size) + "\nPrice: " + str(spend.hold) + "\n"
			print target.msg
			#sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test",target.msg,"nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')

			target.state = 2
			gui.curPrice.config(text=str(target.state))
			gui.top.update()
		if target.state == 2:
			return


def sell(target,spend,gui,ellis,out,raw):
	while(1):
		if target.state == 2:
			spend.cost = 4.95 + (spend.size * 0.65)
			spend.profit =  ((spend.size * 100)) * (float(target.bid) - float(spend.hold)) - (float(spend.cost) * 2)
			time.sleep(1)
			if(spend.profit > 20):	
				target.state = -2
				gui.curPrice.config(text=str(target.state))
				gui.top.update()
				print "Today profit is: ", spend.profit
				ellis.fakeCash += spend.profit
				target.msg = "Cash: " + str(ellis.fakeCash)
				#sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test",str(target.msg),"nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')

				#writeTo(raw,str(ellis.fakeCash))
				#appendTo(out,str(spend.profit))
		if target.state == -2:
			return


def calcProfit(gui,spend,target):
	while(1):
		if target.state == 3:
			spend.cost = 4.95 + (spend.size * 0.65)
			spend.profit =  ((spend.size * 100) * (target.bid - spend.hold)) - (spend.cost * 2)
			#print "Profit: ", spend.profit
			gui.profitPrice.config( text=str(round(spend.profit,2)))

def setAccount(s,ellis,gui):

	root = ET.fromstring(s)

	for child in root.iter('accountbalance'):
		ellis.number = child.find('account').text 
		ellis.value = child.find('accountvalue').text 
		ellis.cash = child.find('money').find('cashavailable').text

	configAccountValue(gui,ellis)


def read_stream(ui,target,putTarget):
	while(target.state == -1):
		time.sleep(1)
		print "Steam is Sleeping"
	temp = ["",""]
	a = ["","",""]
	b = ["","",""]
	buffAsk = ""
	buffBid = ""
	buffSym = ""
	ask = ""
	bid = ""
	sym = ""
	insideAsk = False
	insideBid = False
	insideSym = ""
	s = requests.Session()
	s.auth = OAuth1(constant.ALLY_CONSUMER_KEY, constant.ALLY_CONSUMER_SECRET, constant.OAUTH_TOK, constant.OAUTH_TOK_SEC, signature_type='auth_header',timestamp="0")
	symbols = [target.name,putTarget.name]
	#symbols = ["SPY181107C00277000","SPY181107P00271500"]
	payload = {'symbols': ','.join(symbols)}
	headers = {'connection': 'keep-alive', 'content-type': 'application/json', 'x-powered-by': 'Express', 'transfer-encoding': 'chunked'}

	resp = s.get('https://stream.tradeking.com/v1/market/quotes.xml', stream=True, params=payload)

	print resp

	for line in resp.iter_lines():
		if line:
			#print line
			l = list(line)
			parseStream(ui,temp,a,b,l,insideAsk,insideBid,insideSym,buffBid,buffAsk,buffSym,ask,bid,sym,target,putTarget)

def parseStream(ui,temp,a,b,l,insideAsk,insideBid,insideSym,buffBid,buffAsk,buffSym,ask,bid,sym,target,putTarget):
	for i in l:
				if insideSym == True:
					if i == "<":
						insideSym = False
						buffSym = ""
						if a[2] == "":
							a[2] = sym
							a[0] = temp[0]
							a[1] = temp[1]
						else:
							if a[2] != sym:
								b[2] = sym
								b[0] = temp[0]
								b[1] = temp[1]
							else:
								a[0] = temp[0]
								a[1] = temp[1]
						sym = ""
					else:
						sym += i
				else:
					if buffSym == "":
						if i == 's':
							buffSym += i
					else:		
						if buffSym == "s":
							if i == "y":
								buffSym += i
						if buffSym == "sy":
							if i == "m":
								buffSym += i
						if buffSym == "sym":
							if i == "b":
								buffSym += i
						if buffSym == "symb":
							if i == "o":
								buffSym += i
						if buffSym == "symbo":
							if i == "l":
								buffSym += i
						if buffSym == "symbol":
							if i == 's':
								buffSym = ""
							if i == ">":
								buffSym += i

						if buffSym == "symbol>":
							insideSym = True
				if insideBid == True:
					if i == "<":
						insideBid = False
						buffBid = ""
						#print bid
						temp[1] = bid
						bid = ""
					else:
						bid += i
				else:
					if buffBid == "":
						if i == 'b':
							buffBid += i
					else:		
						if buffBid == "b":
							if i == "i":
								buffBid += i
						if buffBid == "bi":
							if i == "d":
								buffBid += i
						if buffBid == "bid":
							if i == 's':
								buffBid = ""
							if i == ">":
								buffBid += i

						if buffBid == "bid>":
							insideBid = True
				if insideAsk == True:
					if i == "<":
						insideAsk = False
						buffAsk = ""
						#print ask
						temp[0] = ask
						ask = ""
					else:
						ask += i
				else:
					if buffAsk == "":
						if i == 'a':
							buffAsk += i
					else:		
						if buffAsk == "a":
							if i == "s":
								buffAsk += i
						if buffAsk == "as":
							if i == "k":
								buffAsk += i
						if buffAsk == "ask":
							if i == 's':
								buffAsk = ""
							if i == ">":
								buffAsk += i

						if buffAsk == "ask>":
							insideAsk = True
	#print a,b
	if a[2] != "":
		q = list(a[2])
		if q[9] == 'C':
			if a[0] != "":
				target.ask = a[0]
			if a[1] != "":
				target.bid = a[1]
			if b[0] != "":
				putTarget.ask = b[0]
			if b[1] != "":
				putTarget.bid= b[1]

		else:
			if b[0] != "":
				target.ask = b[0]
			if b[1] != "":
				target.bid = b[1]
			if a[0] != "":
				putTarget.ask = a[0]
			if a[1] != "":
				putTarget.bid= a[1]
	target.mid = round((float(target.ask) + float(target.bid))/2,2)
	putTarget.mid = round((float(putTarget.ask) + float(putTarget.bid))/2,2)

def configAccountValue(gui,ellis):
	gui.accountPrice.config(text=str(ellis.value))

def readFakeCash(file):

	fp = open(file,"r")
	content = fp.read()
	fp.close()
	return float(content)

def writeTo(file,value):

	fp = open(file,"w")
	fp.write(value)
	fp.close()

def appendTo(file,value):
	fp = open(file,"a")
	fp.write("\n")
	fp.write(value)
	fp.close()






