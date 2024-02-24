



#




#


#



#




#



#



for _ in range(int(input())):
    count  = 0
    string = input().lower()
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    print(count)
