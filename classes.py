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

class spend:
	hold = 0.0
	profit = 0.0
	cost = 0.0
	size = 0
	isSold = False

class option:
	tick = "SPY"
	year = "18"
	date = ""
	month = ""
	call = ""
	strike = ""
	symbol = ""

class gui:
	top = Tk()
	askLabel = Label(top, text="ask",bg='grey')
	bidLabel = Label(top, text="bid",bg='grey')
	midLabel = Label(top, text="mid",bg='grey')
	acountLabel = Label(top, text="Account Value: ",bg='grey')
	holdLabel = Label(top, text="Hold: ",bg='grey')
	curLabel = Label(top, text="Cur: ",bg='grey')
	profitLabel =  Label(top, text="Profit: ",bg='grey')

	accountPrice = Label(top, text="0.0",bg='cyan')
	askPrice = Label(top, text="0.0",bg='cyan')
	bidPrice = Label(top, text="0.0",bg='cyan')
	midPrice = Label(top, text="0.0",bg='cyan')
	holdPrice = Label(top, text="0.0",bg='cyan')
	profitPrice = Label(top, text="0.0",bg='cyan')
	curPrice = Label(top, text="0.0",bg='cyan')
