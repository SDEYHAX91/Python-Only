def isPrime(num):
    '''Checks whether the given number is prime or not'''
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def genPrimeNos(n):
    '''Generate prime numbers iteratively up to n primes.'''

    primes = []
    num = 2

    while len(primes) < n:  
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes
