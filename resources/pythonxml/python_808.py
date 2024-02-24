




#


#

#

#



#



for _ in range(int(input())):
    string = input()
    count = 0
    for i in range(len(string)):
        if string[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    print(count)
