'''Numbers which are divisible by sum of their digits'''

def isHarshadNo(num):
    sum = 0
    temp = num # Creating temp for sum of digits 
    # to avoid ambiguity
    
    while temp > 0: #Sum of digits
        sum += temp % 10
        temp //= 10
    
    # True if num divisible by sum of digits
    return True if num % sum == 0 else False 
