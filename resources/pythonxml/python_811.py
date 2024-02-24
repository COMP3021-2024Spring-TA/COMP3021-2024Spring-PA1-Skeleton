

#




#


#




#







for _ in range(int(input())):
    roads = int(input())
    lst = set([])
    for i in range(roads):
        node1,node2 = map(int,input().split())
        lst.add(node1)
        lst.add(node2)
    print(len(lst))
