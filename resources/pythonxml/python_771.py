




#



#


#




#





#




def isPrime(x):
    i = 2
    while (i < x):
        if (x%i == 0):
            return False
        i += 1
    return True

def check(n):
    c = 1
    while not(isPrime(c+n)):
        c += 1
    return c

testCases = int(input())
while testCases:
    testCases -= 1
    x,y = map(int,input().split())
    n = x + y
    print (check(n))
