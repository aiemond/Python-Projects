'''
Given two integer arrays num1 and num2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in num1 and num2 respectively.
Merge num1 and num2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''


def merge (num1,num2,m,n):
    i= m-1
    j= n-1
    k = m+n-1
    
    while i >= 0 and j >= 0:
        if num1[i] > num2 [j]:
            num1 [k] = num1 [i]
            i -= 1
        else:
            num1 [k]= num2 [j]
            j -= 1
        k -=1

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
merge(num1,num2, 3, 3)
print("Output:", num1)     # Output: [1, 2, 2, 3, 5, 6]
