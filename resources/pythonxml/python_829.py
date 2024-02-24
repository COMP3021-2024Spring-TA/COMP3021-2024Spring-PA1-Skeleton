

#

#


#


#

#

#

#








testCase1 = int(input())
a = input().split()
testCase2 = int(input())
b = input().split()
c = list(set(a) - set(b))
c.sort()
for i in c:
	print(int(i), end = ' ')
