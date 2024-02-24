

#


#

#



#



#




#






#





testCases = int(input())
while testCases:
    testCases -= 1
    M, W = map(str, input().split())
    countM = 1
    countW = 1
    for i in M:
        result = W.find(i)
        if result == -1:
            countM = 0
            break
    for i in W:
        result = M.find(i)
        if result == -1:
            countW = 0
            break
    if (countM == 1) or (countW == 1):
        print('YES')
    else:
        print('NO')
