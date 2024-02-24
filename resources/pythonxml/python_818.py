



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
while testCases:
    testCases -= 1
    website = input()
    website = website.replace('www.', '')
    website = website.replace('.com', '')
    website = list(website)
    count = len(website)
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in website:
        if i not in vowels:
            cnt += 1

    print(str(cnt + 4) + '/' + str(count + 8))
