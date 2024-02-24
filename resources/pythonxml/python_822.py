









#

#



#

#



#

#




#




while(True):
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if b-a == c-b:
        print ('AP', c + b - a)
    else:
        print ('GP', c * (b // a))
