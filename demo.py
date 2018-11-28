import matplotlib.pyplot as plt
import matplotlib.animation as ani
from Tkinter import *

fig = plt.figure()
ax1 = fig.add_subplot(111)

file = "spyQA.txt"
arr = []
hold = []

list12 = []
list26 = []
listmacd = []
listsig = []

def calc12():
	temp = 0.0
	count = 0
	count12 = 0
	for i in range(12):
		temp += float(arr[count])
		count += 1

	temp /= 12
	#temp = round(temp,2)

	#print temp

	list12.append(temp)

	for i in  range(len(arr) - 12):
		result = 0.0
		#print "arr = ", float(arr[count])
		#print "list12 = ", list12[count12]
		result = (float(arr[count]) * (2.0/13.0))  + (list12[count12] * (1.0 - (2.0/13.0)))
		count += 1
		count12 += 1
		#result = round(result,2)
		#print result
		list12.append(result)

def calc26():
	temp = 0.0
	count = 0
	count26 = 0
	for i in range(26):
		temp += float(arr[count])
		count += 1

	temp /= 26
	#temp = round(temp,2)

	#print temp

	list26.append(temp)

	for i in  range(len(arr) - 26):
		result = 0.0
		#print "arr = ", float(arr[count])
		#print "list12 = ", list12[count12]
		#print i
		result = (float(arr[count]) * (2.0/13.0))  + (list26[count26] * (1.0 - (2.0/13.0)))
		count += 1
		count26 += 1
		#result = round(result,2)
		#print result
		list26.append(result)

def calcMACD():
	count12 = 11;
	count26 = 0;
	for i in range(len(list26)):
		res = list12[count12] - list26[count26]
		#print res
		listmacd.append(res)
		count12 += 1
		count26 += 1

def calcSignal():

	count = 0
	temp = 0.0
	countsign = 0
	for i in range(9):
		temp += listmacd[count]
		count += 1

	temp /= 9

	listsig.append(temp)

	for i in  range(len(listmacd) - 9):
		result = 0.0
		#print "arr = ", float(arr[count])
		#print "list12 = ", list12[count12]
		#print i
		result = (float(listmacd[count]) * (2.0/13.0))  + (listsig[countsign] * (1.0 - (2.0/13.0)))
		count += 1
		countsign += 1
		#result = round(result,2)
		print result
		listsig.append(result)

def refresh(i):
	print "refreshing..."
	ax1.clear()
	
	#ax1.plot(arr)
	#ax1.plot(list26)
	#ax1.plot(list12)
	ax1.plot(listsig)
	#ax1.plot(listmacd)

if __name__ == "__main__":

	line = open(file,"r").read()
	for l in line:
		if l != '\n':
			hold.append(l)
		if l == '\n':
			i = "".join(hold)
			if i != "0.0":
				arr.append(i)
			for i in range(len(hold)):
				hold[i] = ""

	calc26()
	calc12()
	calcMACD()
	calcSignal()

	#a = ani.FuncAnimation(fig,refresh,interval=3000)
	#ax1.plot(arr)
	#ax1.plot(list26)
	#ax1.plot(list12)
	#ax1.plot(listsig


	plt.subplot(2, 1, 1)
	plt.plot(arr)
	plt.plot(list12)
	plt.plot(list26)
	plt.title('A tale of 2 subplots')
	plt.ylabel('Damped oscillation')

	plt.subplot(2, 1, 2)
	plt.plot(listsig)
	plt.xlabel('time (s)')
	plt.ylabel('Undamped')
	plt.show()




