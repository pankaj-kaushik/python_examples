s = "abc"
t = [0,1,2]

u = zip(s, t)

print "list of tuples", u

print "list of tuple using tuple assignment"

for i, j in u:
    print i, j

print "printing index and value at same time"
    
v = enumerate(s)

for index, value in v:
    print index, value