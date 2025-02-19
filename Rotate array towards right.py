def ArrayRotationRight(arr, k):
        n = len(arr)
        
        if k < 0: #If k is -ve, it is converted into +ve integer
            k = abs(k)
        if k > n: #Make sure k is less than array size
            k %= n #to minimize no. of rotations

  # Last 2 parts will be at the 1st, reamining elements will be at the last
        front = arr[-k:] # Split the array into two parts and concatenate them
        back = arr[:-k]
        arr[:] = front + back
