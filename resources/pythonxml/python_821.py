

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






T = int(input())
if(T>=1 and T<=10):

    for i in range(0,T):
        flag1=0
        flag2=0
        as1 = input()
        bs = input()

        #a = list(as1.split())
        #b = bs.split()

        for i in range(97,97+26):
            if(as1.count(chr(i))>bs.count(chr(i))):
                flag1=1
            elif(as1.count(chr(i))<bs.count(chr(i))):
                flag2=1
            if (flag1==1 and flag2==1):
                break
        #a = "".join(a)
        #b = "".join(b)

        if(flag1==1 and flag2==0):
            print("You win some.")
        elif(flag1==0 and flag2==1):
            print("You lose some.")
        else:
            print("You draw some.")
