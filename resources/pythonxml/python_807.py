
#

#



#

#

#



#

#

#


#





#





for _ in range(int(input())):
    string = input()
    sumit_string = True
    check = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(string) - 1):
        check_first = check.find(string[i]) + 1
        check_second = check.find(string[i + 1]) + 1
        if abs(check_second - check_first) == 1 or abs(check_second - check_first) == 25:
            continue
        else:
            sumit_string = False
            break

    if sumit_string:
        print('YES')
    else:
        print('NO')
