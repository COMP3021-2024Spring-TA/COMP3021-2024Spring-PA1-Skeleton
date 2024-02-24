



#



#




#



#







#







def enqueue(myList, element):
  myList.insert(0, element)

def dequeue(myList):
  if len(myList) > 0:
    return myList.pop()
  else:
    return -1

myList = []

for _ in range(int(input())):
    userInput = input().split()
    if userInput[0] == 'E':
      enqueue(myList, int(userInput[1]))
      print(len(myList))
    else:
      deleted = dequeue(myList)
      print(deleted, len(myList))
