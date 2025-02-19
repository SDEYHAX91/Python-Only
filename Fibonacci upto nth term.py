# 1. With List
def fibonacci(n):
    '''Generate Fibonacci series upto nth term'''
    fib_seq = [] #With List Iteratively
    a,b = 0,1
    for i in range(n):
        fib_seq.append(a)
        a,b = b,a+b
    return fib_seq

# 2. Without List but iterative
def Fibonacci(n):
    if n <= 0: #If n less than equal to 0
        return
    else:
        a,b = 0,1
        for i in range(n):
            print(a, end = ' ')
            a,b = b,a+b
