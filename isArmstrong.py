# CHECK WHETHER GIVEN NUMBER IS ARMSTRONG NUMBER OR NOT
def isArmstrong(num):
    no_digits = len(str(num)) #No. of no_digits
     
    sum_pow_digits = 0 # Sum of power of no_digits
     
    while num > 0:
        digit = num % 10 
        sum_pow_digits += digit ** no_digits
        num //= 10
         
    return num == sum_pow_digits
