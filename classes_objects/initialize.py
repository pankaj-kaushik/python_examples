class Hello:
    x = 20
    def show(self):
        print "Function show is called"
        
    
obj = Hello()
print Hello.x  #class variable

print obj.x

#trivial way of accessing methods
obj.show()    #instance variable
print Hello.show is obj.show

Hello.show(obj)