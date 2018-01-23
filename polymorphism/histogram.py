#below function will count occurrence of given item in a sequence

def get_item_count(seq):
    """
    This function can work on any sequence, tuple, list or string.
    It is a poly-morphic function
    """
    res = {}
    for item in seq:
        if item not in res:
            res[item] = 1
        else:
            res[item] = res[item] + 1
    return res

print get_item_count([1,2,3,4,4,2])