def outer():
    x = "outer x"
    
    def inner():
        #nonlocal x    #nonlocal is defined in python 3
        x = 'inner x'
        print x
    inner()
    print x

outer()