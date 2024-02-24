





























def countingSort(myList):
    maxValue = 0
    for i in range(len(myList)):
        if myList[i] > maxValue:
            maxValue = myList[i]

    buckets = [0] * (maxValue + 1)

    for i in myList:
        buckets[i] += 1

    i = 0
    for j in range(maxValue + 1):
         for a in range(buckets[j]):
             myList[i] = j
             i += 1

    return myList

if __name__ == '__main__':
    sortedList = countingSort([1,23,4,5,6,7,8])
    print(sortedList)
