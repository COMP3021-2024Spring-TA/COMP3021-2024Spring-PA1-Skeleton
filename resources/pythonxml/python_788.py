






#



#


#



#






#





#






testCases = int(input())
for _ in range(testCases):
    M, P = map(int, input().split())
    c = M ^ P
    result = 0
    while(c > 0):
        result += c % 2
        c //= 2
    print(result)









#



