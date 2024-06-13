"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""
import math

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return 'number can not be negative'
        
        factorial = 1
        for i in range(2, number + 1): 
            factorial *= i
            
        count = 0
        while factorial % 10 == 0:
            count += 1
            factorial //= 10
        return count
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.find_tailing_zeroes(7)
    print(f"Result: {result}")