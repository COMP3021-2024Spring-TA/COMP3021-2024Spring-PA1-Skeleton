


#



#

#





#

#

#




#


#










#





L = int(input())
N = int(input())
while N:
    N -= 1
    W, H = map(int, input().split())
    if W < L or H < L:
        print('UPLOAD ANOTHER')
    elif W != H:
        print('CROP IT')
    else:
        print('ACCEPTED')
