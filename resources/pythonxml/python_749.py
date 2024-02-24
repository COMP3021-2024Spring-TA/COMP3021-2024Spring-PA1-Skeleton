#Author: OMKAR PATHAK

#This program illsutrates an example of N-ary search

ARRAY_SIZE = 10000000       
DIVISIONS = 10              

def Main():
    myArray = []
    for i in range(0, ARRAY_SIZE + 1):
        myArray.insert(i, i)

    key = int(input('Enter the key to search:'))

    low = 0
    high = ARRAY_SIZE
    found = 0

    if(key < myArray[low] or key > myArray[high - 1]):
        print('Key is out of range!')
    else:
        while(low < high):
            if(key == myArray[low] or key == myArray[high]):
                found = 1
                break
            else:
                partitionSize = (high - low) // DIVISIONS
                print('Searching from {} to {}'.format(low, high))
                print('Array Size is: ',(high - low))

                mid = [0]
                for i in range(1, DIVISIONS + 1):
                    mid.insert(i,low + partitionSize * i)
                    if(key == myArray[mid[i]]):
                        found = 1
                print()
                if(found):
                    break

                if(key < myArray[mid[1]]):
                    high = mid[1] - 1
                elif(key > myArray[mid[DIVISIONS - 1]]):
                    low = mid[DIVISIONS - 1] + 1
                else:
                    for i in range(2, DIVISIONS + 1):
                        if(key < myArray[mid[i]]):
                            low = mid[i - 1] + 1
                            high = mid[i];
                            break;

    if(found):
        print('Element Found!')
    else:
        print('Not Found!')

if __name__ == '__main__':
    Main()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
