# FIND ARMSTRONG NUMBERS BETWEEN INTERVALS
def FindArmstrong(low, high): 
     
    for num in range(low, high + 1): #Iterate over intervals
        no_digits = len(str(num)) #No. of no_digits
        sum_pow_digits = 0 # Sum of power of no_digits
        temp = num
    
        while temp > 0: #Find Armstrong
            digit = temp % 10 
            sum_pow_digits += digit ** no_digits
            temp //= 10
        
        if num == sum_pow_digits: #If true print as output
            print(num, end = ' ')
