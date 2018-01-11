def show(a, *args, **kwargs):
    print "Function print() is called with following arguments"
    print a
    print "Now variable number of arguments are as :"
    print "-" * 50
    for i in args:
        print i,
    print "\nNow variable number of keyword arguments are as :"
    print "-" * 50
    keys = kwargs.keys()
    keys.sort()
    for kw in keys:
        print kw, ' : ', kwargs[kw]
        
show("hello", "Ram", "shyam", len=2, widht=4)