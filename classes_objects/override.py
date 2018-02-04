class B:
    pass
class A(object):
    def __init__(self):
        print "Constructor fired"
        self.x = 30 #data member having same method name
    def x(self):
        print "function x() is called"
    
obj = A()
print obj.x #It will override the member function with the same name

obj_b = B()
print type(obj), type(A)
print type(obj_b), type(B)