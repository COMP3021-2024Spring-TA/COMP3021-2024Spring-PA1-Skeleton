


















a=int(input())
b=list(map(int,input().split()))
d=b[0]
for i in range(1,len(b)):
    d=d^b[i]
print(d)
