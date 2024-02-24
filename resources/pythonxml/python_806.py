
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



string = list(input())
result = []
for i in range(len(string)):
    if string[i] not in result:
        result.append(string[i])

print(''.join(result))
