def mysum(seq):
    def add(x, y): return x + y
    return reduce(add, seq, 3)

print mysum(range(1,5))