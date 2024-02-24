

#



#




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
    N, K = map(int, input().split())
    if  K > 0:
        print((N // K), (N % K))
    else:
        print(0, N)
