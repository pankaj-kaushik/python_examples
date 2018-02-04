import threading
import time



def getFact(num):
    print "calculating factorial of ", num, " = ",
    fact = 1
    while num > 0:
        print "in getFact"
        fact = fact * num
        num = num - 1
        time.sleep(0.2)
        
    print "factorial = ", fact

def isEven(num):
    print "Checking even no"
    if num % 2 == 0:
        print "num is even number"
    else:
        print "num is odd number"

def getSum(num):
    total = 0
    for i in xrange(1,num):
        print "in getSum"
        total = total + i
        time.sleep(0.2)
        
    print "sum = ", total

start_time = time.clock()

t1 = threading.Thread(target=getFact, args=(4,))
t2 = threading.Thread(target=getSum, args=(5 ,))

t1.start()
t2.start()

t1.join()
t2.join()

print "Program Ends, Total Time Taken : ", time.clock() - start_time

