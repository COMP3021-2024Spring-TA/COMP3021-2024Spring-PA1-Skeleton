



#


#




#


#



#












testCases = int(input())
for _ in range(testCases):
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            result = i ^ j
            if result <= n:
                count += 1

    print(count)
