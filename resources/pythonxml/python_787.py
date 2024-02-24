























for _ in range (int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    ans=0
    a2=0
    for i in range(0,a):
        if(b[i]&1):
            ans+=1
        else:
            a2+=1
        
    print(ans*a2)
