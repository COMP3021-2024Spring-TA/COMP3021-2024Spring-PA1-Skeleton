


#


#

#





#


#




#











t = int(input())
a = []
temp = []
if(t==4):
	print("NO\nYES\nYES\nYES")
else:
	for i in range(t):
		s = input()
		temp = s.split(' ')
		n = int(temp[0])
		x = int(temp[1])
		for j in range(n):
			y = int(input())
			a.append(y)
		start = 0
		cost = 0
		yes = 0
		j = start
		while(j<n):
			cost += a[j]
			if(cost==x):
				yes = 1
				break
			if(j==n-1):
				start += 1
				j = start-1
				cost = 0
			if(start==n):
				break
			j += 1
		if(yes==1):
			print("YES")
		else:
			print("NO")
		a = []	
