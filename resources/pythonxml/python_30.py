def strcmp(str1, str2):
    index1, index2 = 0, 0
    while index1 < len(str1) and index2 < len(str2):
        if ord(str1[index1]) == ord(str2[index2]):
            index1 += 1
            index2 += 1
        elif ord(str1[index1]) < ord(str2[index2]):
            return -1
        else:
            return 1
    
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0