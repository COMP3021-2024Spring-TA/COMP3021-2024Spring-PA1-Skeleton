


#


#

#


#


#

#


#





#





testCases = int(input())
for _ in range(testCases):
    suvojit = 0
    suvo = 0
    s = input()
    suvojit = s.count("SUVOJIT")
    suvo = s.count("SUVO")
    print('SUVO = ',suvo-suvojit,', SUVOJIT = ',suvojit,sep='')
