class items:
    def __init__(self):
        self.mylist = [1, 2, 3]
        self.index = -1
    
    def __iter__(self):
        return self
    
    def next(self): #in python 3, this method has changed to __next__
        self.index += 1
        if self.index == len(self.mylist):
            raise StopIteration
        
        return self.mylist[self.index]
    

r = items()



itr = iter(r)

print r, itr

print next(itr)
print next(itr)
print next(itr)

#for i in items():
for i in r:
    print i