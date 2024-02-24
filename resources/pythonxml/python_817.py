
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
    N = int(input())
    count = 0
    result = 0
    string = input()
    for i in string:
        if i.isdigit():
            count += 1
        else:
            if count >= 1:
                result += 1
                count = 0

    print(result)
