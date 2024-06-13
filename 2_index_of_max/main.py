"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) == 0:
            return 'list can not blank'
        
        max_number = 0
        for number in numbers:
            if number > max_number:
                max_number = number

        max_number_index = numbers.index(max_number)
        return max_number_index
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.find_max_index([1,2,1,3,5,6,4])
    print(f"Result: {result}")