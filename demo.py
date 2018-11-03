import threading

num = 0;
lock = threading.Lock()

def add():
	global num
	for i in range(5):
		#lock.acquire()
		num += 1
		print num
		#lock.release()



if __name__ == "__main__":

	var = 5

	print (var == 5) and (var != 0)

	#t1 = threading.Thread(target=add)
	#t2 = threading.Thread(target=add)
	#t3 = threading.Thread(target=add)

	#t1.start()
	#t1.join()
	#t2.start()
	#t2.join()
	#t3.start()
	