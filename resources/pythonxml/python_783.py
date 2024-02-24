

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

#


for i in range(int(input())):
        L, D, S, C = map(int,input().split())
        for j in range(1, D):
                S = S + C * S
                if S >= L:
                        break
        if L <= S:
                print("ALIVE AND KICKING")
        else:
                print("DEAD AND ROTTING")  
