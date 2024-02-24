

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
    G = int(input())
    while G:
        G -= 1
        I, N, Q = map(int, input().split())
        if N % 2 == 0:
            print(N // 2)
        else:
            if I == Q:
                print(N // 2)
            else:
                print((N // 2) + 1)
