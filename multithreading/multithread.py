import threading
import time



def getFact(num):
    print "calculating factorial of ", num, " = ",
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    print fact

def isEven(num):
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

