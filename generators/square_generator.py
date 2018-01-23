# def square(x):
#     for i in x:
#         yield i*i
# 
# 
# my_nums = square([1,2,3,4,5])
#print my_nums   #it is a generator object

my_nums = [i*i for i in [1,2,3,4,5]]
print my_nums   #it is a list

my_nums = (i*i for i in [1,2,3,4,5])
print my_nums   #it is a generator object

#print list(my_nums)

for i in my_nums:
    print i