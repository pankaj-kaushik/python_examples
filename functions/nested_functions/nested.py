def addOne(myFunc):
    def addOneInside(*args, **kwargs):
        return myFunc(*args, **kwargs) + 1
    return addOneInside

@addOne
def oldFunc(x = 3245):
    return x

newfunc = addOne(oldFunc)
print oldFunc(), newfunc()

# Instead of doing below, we can add decorator on the definition of oldFunc()
#oldFunc = addOne(oldFunc)

print oldFunc() # It will print 4