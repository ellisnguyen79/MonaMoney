from Tkinter import *

class User:
	value = 0.0
	number = 0
	cash = 0.0
	faskCash = 0.0

class info:
	ask = 0.0
	bid = 0.0
	mid = 0.0
	support = 0.0
	resist = 0.0
	state = -1
	msg = ""
	name = ""

class spend:
	hold = 0.0
	profit = 0.0
	cost = 0.0
	size = 0
	isSold = False
	win = 0
	lose = 0
	total = 0.0

class option:
	tick = "SPY"
	year = "18"
	date = ""
	month = ""
	call = ""
	strike = ""
	symbol = ""
	bidCall = ""
	bidPut = ""
	askCall = ""
	askPut = ""

class gui:
	top = Tk()
	askLabel = Label(top, text="ask",bg='grey')
	bidLabel = Label(top, text="bid",bg='grey')
	midLabel = Label(top, text="mid",bg='grey')
	acountLabel = Label(top, text="Account Value: ",bg='grey')
	holdLabel = Label(top, text="Hold: ",bg='grey')
	curLabel = Label(top, text="Cur: ",bg='grey')
	profitLabel =  Label(top, text="Profit: ",bg='grey')

	#put
	putaskLabel = Label(top, text="ask",bg='grey')
	putbidLabel = Label(top, text="bid",bg='grey')
	putmidLabel = Label(top, text="mid",bg='grey')
	putholdLabel = Label(top, text="Hold: ",bg='grey')
	putcurLabel = Label(top, text="Cur: ",bg='grey')
	putprofitLabel =  Label(top, text="Profit: ",bg='grey')

	accountPrice = Label(top, text="0.0",bg='cyan')
	askPrice = Label(top, text="0.0",bg='cyan')
	bidPrice = Label(top, text="0.0",bg='cyan')
	midPrice = Label(top, text="0.0",bg='cyan')
	holdPrice = Label(top, text="0.0",bg='cyan')
	profitPrice = Label(top, text="0.0",bg='cyan')
	curPrice = Label(top, text="0.0",bg='cyan')

	#put
	putaskPrice = Label(top, text="0.0",bg='cyan')
	putbidPrice = Label(top, text="0.0",bg='cyan')
	putmidPrice = Label(top, text="0.0",bg='cyan')
	putholdPrice = Label(top, text="0.0",bg='cyan')
	putprofitPrice = Label(top, text="0.0",bg='cyan')
	putcurPrice = Label(top, text="0.0",bg='cyan')



