
#

#


#

#

#

#







#





def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

testCases = int(input())
for _ in range(testCases):
    number = int(input())
    print(factorial(number))
