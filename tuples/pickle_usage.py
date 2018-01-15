import pickle

t = (1,2,3)

x = pickle.dumps(t)
print x
y = pickle.loads(x)
print y 