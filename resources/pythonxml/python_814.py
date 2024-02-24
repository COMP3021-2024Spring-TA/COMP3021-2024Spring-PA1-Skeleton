

#


#


#









#





testCases = int(input())
while testCases:
    testCases -= 1
    string = input()
    alphabet = list(map(chr, range(97, 123)))
    if set(alphabet) == set(string):
        print('YES')
    else:
        print('NO')
