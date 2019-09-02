def num_to_nums(num):
    res = []
    for s in str(num):
        res.append(int(s))
    return res


print(num_to_nums(20))
