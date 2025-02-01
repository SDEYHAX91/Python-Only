def fibonacci(n):
    '''Generate Fibonacci series till a specified integer'''
    fib_seq = []
    a,b = 0,1
    
    while(a <= n):
        fib_seq.append(a)
        a,b = b, a+b
    
    return fib_seq
