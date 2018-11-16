import matplotlib.pyplot as plt
import matplotlib.animation as ani
from Tkinter import *

fig = plt.figure()
ax1 = fig.add_subplot(111)

file = "spyAsk.txt"
arr = []
hold = []

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
def refresh(i):
	print "refreshing..."
	print arr
	ax1.clear()
	ax1.plot(arr)
a = ani.FuncAnimation(fig,refresh,interval=3000)
plt.show()