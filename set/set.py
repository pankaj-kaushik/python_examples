city = {'new delhi', 'mumbai', 'banglore'}

print city

fruits = set()
fruits.add('banana')
fruits.add('orange')

print fruits

#Note : never initialize set like below 

items = {}  #it is a dictionary
print type(items)

items = {1}
print type(items)

fs = frozenset([1,2,3,4,5,2,3,4])

fs.add(10) # it will generate exception