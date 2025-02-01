def factors(num):
    '''Returns list of 
    factors of a +ve integer'''
    
    factor = []
    if num <= 0:
        return 0
    else:
        for i in range(1,num+1):
            if num % i == 0:
                factor.append(i)
    return factor
