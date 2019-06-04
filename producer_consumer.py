from threading import Thread, Lock

class FlightReservtion:
    l=Lock()
    def __init__(self, ticket_left):
        self.ticket_left=ticket_left

    l.acquire()
    def buy(self, ticket_requested):
        if(self.ticket_left>=ticket_requested):
            print('Yout ticket is confirmed...')
            self.ticket_left-=ticket_requested
        else:
            print('No more tickets left...')
    l.release()


reservation=FlightReservtion(10)
t1=Thread(target=reservation.buy, args=[3])
t2=Thread(target=reservation.buy, args=[5])
t3=Thread(target=reservation.buy, args=[8])
t1.start()
t2.start()
t3.start()