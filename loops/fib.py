def getfib(num):
    a,b = 0, 1
    count = 1
    print "Fibonacci numbers upto ", num, "are : ",
    print a, b,
    while count <= num - 2: #-2 is done because two numbers have already been printed
        a, b = b , a + b
        count = count + 1
        print b,
        

getfib(10)