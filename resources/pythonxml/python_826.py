




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
    a,b = map(int,input().split())
    if b <= 4:
        print(str(pow(a,b))[-1])
    else:
        if b % 4:
            print(str(pow(a,b%4))[-1])
        else:
            print(str(pow(a,4))[-1])
