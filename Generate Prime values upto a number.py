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
    '''Generate Prime numbers upto certain number'''
  primes = []
  for i in range(2,n+1):
    if isPrime(i):
      primes.append(i)
    return primes
