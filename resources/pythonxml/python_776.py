











#





#


#




#












#





testCases = int(input())
for i in range(0, testCases):
    N = input()
    A = list(map(int,input().split()))
    K = int(input())
    result = A[K - 1]
    A = sorted(A)
    for i in range(0, len(A)):
        if (A[i]== result):
            print (i + 1)
