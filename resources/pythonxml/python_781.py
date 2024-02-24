




#



#





#


#











#






testCases = int(input())
while testCases:
    testCases -= 1
    jewel = input()
    stone = input()
    count = 0
    for i in range(0, len(stone)):
        if stone[i] in jewel:
            count += 1

    print(count)
