def generate_names():
    yield "ram"
    yield "shyam"
    

itr = generate_names()

print next(itr)
print next(itr)

#generators also worked with for loops

print '----------using for loop on generator---------------'
for i in generate_names():
    print i
