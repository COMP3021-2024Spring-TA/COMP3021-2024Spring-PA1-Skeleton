

#



#






number1, number2, divisor = map(int, input().split())
count = 0
for i in range(number1, number2 + 1):
    if i % divisor == 0:
        count += 1
print(count)
