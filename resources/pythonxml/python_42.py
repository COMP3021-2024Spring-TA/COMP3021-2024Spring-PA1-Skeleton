def permutations(arr, start, end):
    if start == end:
        print(arr)
        return
 
    for i in range(start, end):
        arr[i], arr[start] = arr[start], arr[i]
        permutations(arr, start + 1, end)
        arr[i], arr[start] = arr[start], arr[i]