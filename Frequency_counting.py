# from collections import Counter

# def count(arr):
#     freq = Counter(arr)
#     return freq

def count(arr):
    freq = {}
    
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
        
    return freq
    
    
    

print(count([1,3,1,2,3,2]))