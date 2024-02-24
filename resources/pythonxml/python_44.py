def algorithm(n):
    cnt = 1
    res = 0
    while cnt < n:
        cnt *= 2
        for i in range(n):
            res += 1
    return res