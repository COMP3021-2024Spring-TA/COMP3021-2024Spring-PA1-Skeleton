

#


#

#



#


#



#


#



n = int(input().strip())
lst = list(map(int,input().split()))
l = []
max_balanced = 0
current_balance = 0

for element in lst:
    if element > 0:
        if current_balance > 0 and len(l):
            current_balance = 0
        l.append(element)
    elif len(l):
        peek_element = l.pop()
        if peek_element == -(element):
            current_balance += 1
        else:
            current_balance = 0
            l = []
        if current_balance > max_balanced:
            max_balanced = current_balance
print(max_balanced * 2)
