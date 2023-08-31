import threading
import time
from multiprocessing import Process,cpu_count



def counter(num):
    count = 0
    while count < num:
        count =+ 1

def main():

    print(cpu_count())
    num = int(input('Enter the number to count to: '))
    a = Process(target=counter, args=(2,))
    a.start()
    
    a.join()

    print("Finished in: ", time.perf_counter(),"seconds")
    print(time.ctime(0))
    print(threading.active_count())

if __name__ == '__main__':
    main()
    
