def getfib(num):
    a,b = 0, 1
    print "Fibonacci numbers upto ", num, "are : "
    for i in xrange(0, num):
        print a
        a, b = b , a + b

getfib(10)