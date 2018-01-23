class Hello:
    x = 20
    def show(self):
        print "Attribute of object is : ", self.x

class Hi:
    x =30
    def show(self):
        print "Attribute of object is : ", self.x





    
obj1 = Hello()
obj2 =  Hi()

# Below is an invalid way of doing it
#Hello.show(obj2)