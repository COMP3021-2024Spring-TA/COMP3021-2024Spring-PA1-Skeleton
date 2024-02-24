

#

#



#

#

#

#




#



#

for _ in range(int(input())):
    user_input = input()
    string = []
    for i in range(len(user_input)):
        if user_input[i] not in string:
            string.append(user_input[i])

    print(''.join(string))
