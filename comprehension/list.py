from boto3.dynamodb.types import NUMBER
numbers = [1,2,3,4,5,6]
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)

print even


#Doing through list comprehension

result = [i for i in numbers if i %2 == 0]

print result

# set example

s = set([10,11,12,14])

result = {i for i in s if i %2 == 0}

print type(result)