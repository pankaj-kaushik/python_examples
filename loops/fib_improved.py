
#this is called memoization

known_fib = {0:0, 1:1}

def getfib(num):
    if num in known_fib:
        print "Returning from know list for value : ", num
        return known_fib[num]
    res = getfib(num -1) + getfib(num -1)
    known_fib[num] = res
    print "adding to known list for : ", num
    return res
    
getfib(5)
print known_fib