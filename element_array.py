#implementing the binary search algorithm to 
# find the target value in a sorted list of numbers

def binary_search (numbers,target):
    
    low,high = 0, len (numbers)-1
    
    while low <= high:
        mid = (low+high)//2
        if numbers [mid]== target:
            return mid
        elif numbers [mid]<target:
            low = mid +1
        else:
            high = mid -1
        
            
        
    return 'number not in the list'

numbers = [1,3,5,7,9,11,13,15]
target = 9

result = binary_search (numbers,target)
print ('Output:',result)

