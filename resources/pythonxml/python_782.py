

#


#


#

#











#


#


#

#

#

#








#







N1, K1 = map(int, input().split())
K = []
for i in range(1, N1 + 1):
    K.append(input())
while K1:
    K1 -= 1
    string = input()
    flag = 0
    for i in range(len(K)):
        if K[i] in string:
            flag = 1
            break
        elif (len(string) >= int(K[i])):
            flag = 1
            break
    if flag == 1:
        print('GOOD')
    else:
        print('BAD')
