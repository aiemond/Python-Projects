#finding first and last number in an ascending sorted array Leetcode (34)

def finding_first_position(numbers,target):
    low , high = 0 , len (numbers)-1
    first_position = -1
    
    while low <= high:
        mid = (low+high)// 2
        if numbers[mid]== target:
            first_position = mid
            high = mid -1 #coz to first position continue searching left side not right side
        elif numbers [mid] < target:
            low = mid +1
        else:
            high = mid -1
            
    if first_position == -1:
        return 'numbers not in the list'
    return first_position
    

    
def finding_last_position(numbers,target):
    low , high = 0 , len (numbers)-1
    last_position = -1
    
    while low <= high:
        mid = (low+high)// 2
        if numbers[mid]== target:
            last_position = mid
            low = mid + 1 #coz to  find last position continue searching right side not left side
        elif numbers [mid] < target:
            low = mid +1
        else:
            high = mid -1
            
    if last_position == -1:        
        return 'numbers not in the list'
    return last_position
    
    
    
numbers = [1,2,2,3,3,3,3,4,4,5,6,7,9]
target = 3

print ('first position:',finding_first_position(numbers,target))
print ('last position:',finding_last_position(numbers, target))

