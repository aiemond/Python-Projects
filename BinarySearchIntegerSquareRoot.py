import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle special cases for x being 0 or 1
        if x == 0 or x == 1:
            return x
        
        # Initialize the search range for the square root
        start, end = 1, x
        
        while start <= end:
            # Calculate the middle point
            mid = start + (end - start) // 2
            
            # Check if mid squared is greater than x
            if mid * mid > x:
                end = mid - 1
            elif mid * mid == x:
                # Found the exact square root
                return mid
            else:
                start = mid + 1
        
        # Return the integer part of the square root
        return end

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test with different values
    test_values = [4, 8, 16, 25, 30,36,49]
    
    for value in test_values:
        result = solution.mySqrt(value)
        print(f"The integer square root of {value} is {result}.")

