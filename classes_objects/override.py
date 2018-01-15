class A:
    def __init__(self):
        print "Constructor fired"
        self.x = 30 #data member havin same method name
    def x(self):
        print "function x() is called"
    
obj = A()
print obj.x #It will override the member function with the same name