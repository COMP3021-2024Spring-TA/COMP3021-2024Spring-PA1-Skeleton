


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

#

#



#






#



#




testCases = int(input())
for _ in range(testCases):
    string1 = input()
    string2 = input()
    count = 0
    for i in string1:
        if i in string2:
            count += 1

    if count == 0:
        print('No')
    else:
        print('Yes')
