













def SieveOfEratosthenes(n):
    primes = [True] * (n + 1)
    p = 2                   

    while(p * p <= n):
        
        if(primes[p]) == True:
            
            for i in range(p * 2, n + 1, p):
                primes[i] = False

        p += 1
        
    
    for i in range(2, n):
        if primes[i]:
            print(i)

if __name__ == '__main__':
    SieveOfEratosthenes(1000)
