import threading
from threading import Thread

def numbers():
	for x in range(10):
		print(x)
		
t1=Thread(target=numbers)
t2=Thread(target=numbers)
t1.start()
t2.start()
