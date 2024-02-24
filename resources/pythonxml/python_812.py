

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


#

#


#


testCases = int(input())
for _ in range(testCases):
    n = int(input())
    string = list(input())
    start = 0
    fixChars = []
    fixChars = ''
    while start < n:
        for i in range(start, len(string) - 1, 2):
            string[i], string[i + 1] = string[i + 1], string[i]
        fixChars.append(string[start])
        start += 1

    print(fixChars)
