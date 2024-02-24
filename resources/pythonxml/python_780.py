

#


#


#




#


#


#


#






#






A, B = map(int, input().split())
C = A - B
if C % 10 == 9:
    C = C - 1
else:
    C = C + 1
print(C)




