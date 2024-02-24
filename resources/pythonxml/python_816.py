




#



#


#




h = 0
a = 0
r = 0
e = 0
c = 0
k = 0
t = 0
slen = int(input())
string = input()
for i in string:
    if i == 'h':
        h += 1
    elif i == 'a':
        a += 1
    elif i == 'r':
        r += 1
    elif i == 'e':
        e += 1
    elif i == 'c':
        c += 1
    elif i == 'k':
        k += 1
    elif i == 't':
        t += 1

h //= 2
e //= 2
a //= 2
r //= 2

result = h
if result > a:
    result = a
if result > r:
    result = r
if result > e:
    result = e
if result > c:
    result = c
if result > k:
    result = k
if result > t:
    result = t

print(result)
