








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
    n = input()
    myList = []
    count = 0
    check = input().split()
    if len(check) == 1:
      print(1)
    else:
      max = int(check[0])
      for i in range(1, len(check) - 1):
          if int(check[i]) <= max:
            count += 1
            max = int(check[i])

      print(count + 1)
