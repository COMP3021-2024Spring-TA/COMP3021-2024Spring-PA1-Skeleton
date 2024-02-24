



#




#



#




#



#



#














q = int(input())
queue = []
def isEmpty():
    return queue == []

for _ in range(q):
    check = input().split()
    if int(check[0]) == 1:
        if isEmpty():
            print('No Food')
        else:
            print(queue.pop())
    else:
        queue.append(int(check[1]))
