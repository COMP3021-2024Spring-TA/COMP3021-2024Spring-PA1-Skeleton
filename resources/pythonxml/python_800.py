


#




#


#



userInput = input()
result = []
for i in userInput:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())

print(''.join(result))
