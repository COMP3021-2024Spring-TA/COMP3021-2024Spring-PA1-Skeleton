

#

#

#

#


#

#






#







testCases = int(input())
for _ in range(testCases):
    string = input()
    check = len(string) // 2    
    for i in range(0, check, 2):
        print(string[i], end = '')
    print()
