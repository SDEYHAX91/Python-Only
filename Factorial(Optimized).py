def Factorial(n):
    if n <= 1: #In case input is 1 or less, return 1
        return 1
    else:
        fact = 1 #Iterative approach
        for i in range(2,n+1):
            fact *= i
    return fact
