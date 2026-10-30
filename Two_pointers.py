def two_pointers(arr, target):
    start, end = 0, len(arr)-1
    
    
    while start < end:
        total = arr[start] + arr[end]
        
        if total == target:
            return [start, end]
        
        if total < target:
            start += 1
            
        else:
            end -= 1
        
    return -1   


print(two_pointers([1, 2, 4, 6, 8, 9], 10)) 