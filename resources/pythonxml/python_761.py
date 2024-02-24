










def perfectNumber(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return sum == number

if __name__ == '__main__':
    print(perfectNumber(6)) 
    print(perfectNumber(3)) 
