def sum(seq):
    def add(x, y): return x + y
    return reduce(add, seq, 3)

print sum(range(1,5))