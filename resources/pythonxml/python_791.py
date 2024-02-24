

#




#


#



#


#




#



#



n, x = map(int, input().split())
questions = input().split()
count = 0
skip = 0
for i in range(n):
  if int(questions[i]) > x:
      skip += 1
  else:
    if skip == 2:
      break
    count += 1

print(count)
