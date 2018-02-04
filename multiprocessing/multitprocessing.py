import multiprocessing
import time

def square(num):
    for i in num:
        print "Square of ", i, " = ", i*i
        time.sleep(0.2)

def cube(num):
    for i in num:
        print "Cube of ", i, " = ", i*i*i
        time.sleep(0.2)
    
