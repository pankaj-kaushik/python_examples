my_items = ['shampoo', 'oil', 'cream']

#for i in my_items:
#    print i

itr = iter(my_items)

print next(itr)
print next(itr)
print next(itr)

#printing elements in reverse order_blocks

newitr = reversed(my_items)
print next(newitr)
print next(newitr)
print next(newitr)
