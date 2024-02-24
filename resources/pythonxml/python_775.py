

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

def gcd(firstNumber, secondNumber):
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)
    if firstNumber < secondNumber:
        smaller = firstNumber
    else:
        smaller = secondNumber

    for i in range(1, smaller + 1):
        if (firstNumber % i == 0) and (secondNumber % i == 0):
          gcd = i

    return gcd

for _ in range(int(input())):
    count =  int(input())
    array = input().split()
    currentGCD = array[0]
    flag = 0
    size = 0
    for i in array:
        currentGCD = gcd(i, currentGCD)
        if currentGCD == 1:
            flag = 1
            print(count)
            break

    if flag == 0:
        print(-1)