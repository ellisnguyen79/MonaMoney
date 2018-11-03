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

def tester():
	print "Working"

def buildUI(ui):
	ui.top.geometry("500x500")
	ui.acountLabel.place(x=125,y=0,width=130,height=25)
	ui.accountPrice.place(x=255,y=0,width=150,height=25)
	ui.askLabel.place(x=80,y=80,width=50,height=25)
	ui.askPrice.place(x=130,y=80,width=50,height=25)
	ui.bidLabel.place(x=80,y=105,width=50,height=25)
	ui.bidPrice.place(x=130,y=105,width=50,height=25)
	ui.midLabel.place(x=80,y=130,width=50,height=25)
	ui.midPrice.place(x=130,y=130,width=50,height=25)


	ui.holdLabel.place(x=80,y=185,width=50,height=25)
	ui.holdPrice.place(x=130,y=185,width=50,height=25)
	ui.profitLabel.place(x=80,y=240,width=50,height=25)
	ui.profitPrice.place(x=130,y=240,width=100,height=25)
	ui.curLabel.place(x=190,y=185,width=50,height=25)
	ui.curPrice.place(x=240,y=185,width=50,height=25)


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

def begin(target):

	while(1):
		time = datetime.datetime.today().weekday()
		hour = datetime.datetime.now().hour
		if target.state == -1:
			if time < 5 and hour > 6 and hour < 13:
				target.state = 0
				sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test","Market is open","nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')


# setBuy(spend,ui.holdPrice)

def setBuy(spend,holdPrice):
	holdPrice.config( text=str(spend.hold))

#readAsk(ref,target,ui.askPrice,ui,spend)

def readAsk(ref,target,askPrice,spend):
	while(1):
		time.sleep(0.5)
		if target.state == 0 or target.state == 3:
			print "In readAsK: "
			r = ref.get(constant.SPY_Quote + constant.spy)
			#print r.content
			root = ET.fromstring(r.content)
			for child in root.iter('ask'):
				target.ask = float(child.text)
				#print target.ask
			askPrice.config( text=str(target.ask))

#readBid(ref,target,ui.bidPrice,ui,spend)

def readBid(ref,target,bidPrice,spend):
	while(1):
		time.sleep(0.5)
		if target.state == 0 or target.state == 3:
			print "In reabBid: "
			r = ref.get(constant.SPY_Quote + constant.spy)
			root = ET.fromstring(r.content)
			for child in root.iter('bid'):
				target.bid = float(child.text)
				#print target.bid
			bidPrice.config( text=str(target.bid))

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

def findBuy(target,spend,gui,ellis,out,raw):
	while(1):
		if target.state == 2:	

			# DETERMINE

			spend.hold = target.mid

			####


			setSize(spend,ellis)
			#print "we bought this price: " , spend.hold
			setBuy(spend,gui.holdPrice)
			target.msg = "Quantity: ", spend.size, "\nPrice: ",spend.hold , "\n"
			sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test",str(target.msg),"nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')

			target.state = 3
		if target.state == 3:
			return


def sell(target,spend,gui,ellis,out,raw):

	spend.cost = 4.95 + (spend.size * 0.65)
	while(1):
		if target.state == 3:
			time.sleep(0.5)
			print "in sell/profit: "
			spend.profit =  ((spend.size * 100) * (target.bid - spend.hold)) - (spend.cost * 2)
			if((spend.hold + 0.03) < target.bid ):	
				target.state = 4
				print "Today profit is: ", spend.profit
				ellis.fakeCash += spend.profit
				target.msg = "Cash: ", ellis.fakeCash
				sendemail("nguyene0821","ellisnguyen79@gmail.com","","Test",str(target.msg),"nguyene0821","Mywifezen08+",smtpserver='smtp.gmail.com:587')

				writeTo(raw,str(ellis.fakeCash))
				appendTo(out,str(spend.profit))
		if target.state == 4:
			return


def calcProfit(gui,spend,target):
	while(1):
		if target.state == 3:
			spend.cost = 4.95 + (spend.size * 0.65)
			spend.profit =  ((spend.size * 100) * (target.bid - spend.hold)) - (spend.cost * 2)
			#print "Profit: ", spend.profit
			gui.profitPrice.config( text=str(round(spend.profit,2)))


#setAccount(r.content,ellis)

def setAccount(s,ellis,gui):

	root = ET.fromstring(s)

	for child in root.iter('accountbalance'):
		ellis.number = child.find('account').text 
		ellis.value = child.find('accountvalue').text 
		ellis.cash = child.find('money').find('cashavailable').text

	configAccountValue(gui,ellis)


def read_stream():
	s = requests.Session()
	s.auth = OAuth1(constant.ALLY_CONSUMER_KEY, constant.ALLY_CONSUMER_SECRET, constant.OAUTH_TOK, constant.OAUTH_TOK_SEC, signature_type='auth_header',timestamp="0")
	symbols = ["SPY181029C00264000"]
	payload = {'symbols': ','.join(symbols)}
	headers = {'connection': 'keep-alive', 'content-type': 'application/json', 'x-powered-by': 'Express', 'transfer-encoding': 'chunked'}

	resp = s.get('https://stream.tradeking.com/v1/market/quotes.xml', stream=True, params=payload)

	print resp

	for line in resp.iter_lines():
		if line:
			print(line)

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






