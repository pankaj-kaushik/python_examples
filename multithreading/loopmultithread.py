import multiprocessing
import time



def printNaturalNumbers(num):
    print "Natural Numbers"
    for i in range(num):
        print i + 1

def printSquares(num):
    print "Checking even no"
    if num % 2 == 0:
        print "num is even number"
    else:
        print "num is odd number"


start_time = time.clock()

t1 = threading.Thread(target=getFact, args=(4,))
t2 = threading.Thread(target=isEven, args=(4,))

t1.start()
t2.start()

t1.join()
t2.join()

print "Program Ends, Total Time Taken : ", time.clock() - start_time

