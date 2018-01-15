d = {'a' : 0, 'b' : 1, 'c' : 2}

t = d.items()

print "printing dictionary as list of tuples", t

print "printing dictionary as key value pair"
for i, j in t:
    print i, j
    
#creating dictionary from list of Tuple

newdict = dict(zip('a,b,c', range(3)))

print newdict
