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


start_time = time.time()

getFact(4)
isEven(4)

print "Program Ends, Total Time Taken : ", time.time() - start_time

    	
