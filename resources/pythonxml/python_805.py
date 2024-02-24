
#






#


#


#





#






#





#







array = []
for i in range(int(input())):
    array.append(input())

for i in range(len(array)):
    count = 0
    for j in range(0, i + 1):
        if array[j] < array[i]:
            count += 1
    print(count)


n = int(input())
a = []
for i in range(n):
    a.append(input())
    ans = 0
    for j in a:
        if j < a[i]:
            ans += 1
    print(ans)
