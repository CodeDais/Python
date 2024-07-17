import threading
avl_setas=2
class Movies:
    def booking(self,no_of_seats):
        global avl_setas
        if no_of_seats<=avl_setas:
            print(f'{no_of_seats} seats booked successfully by {threading.current_thread().name}')
            avl_setas=avl_setas-no_of_seats
        elif no_of_seats>avl_setas:
            print(f'{threading.current_thread().name} your no_of_setas must be less than or equal to available seats')
        else:
            print('All seats are sold out')
m=Movies()
t1=threading.Thread(target=m.booking,args=(2,),name='Surendra')
t2=threading.Thread(target=m.booking,args=(2,),name='Priyanka')
t1.start()
t2.start()
            
