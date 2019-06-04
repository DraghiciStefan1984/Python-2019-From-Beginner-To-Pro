import threading
from threading import Thread

'''
if threading.current_thread()==threading.main_thread():
	for x in range(10):
		print(x)
else:
	print('This is not the main thread')


def even_number():
	for x in range(20):
		if x%2==0:
			print(x)

t=Thread(target=even_number)
t.start()
'''

def even_odd():
	even_no()
	odd_no()

def even_no():
	for x in range(100):
		if x%2==0:
			print('even: ',x)

def odd_no():
	for x in range(100):
		if x%2!=0:
			print('odd: ',x)

#thread=Thread(target=even_odd)
#thread.start()


class CustomThread(Thread):
	def run(self):
		print('Pyramid')
		for i in range(0, 5):
			for j in range(0, i+1):
				print('*', end=' ')
			print('\r')

c=CustomThread()
c.start()