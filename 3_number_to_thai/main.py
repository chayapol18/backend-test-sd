"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return 'number can not less than 0'
        elif number > 10000000:
            return 'number can not more than 10,000,000'
        
        thai_numbers = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
        thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน', 'สิบล้าน']
        
        if number == 0:
            return thai_numbers[0]
        
        result = ''
        nums = [int(num) for num in str(number)]
        nums.reverse()
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] == 2 and i == 1:
                    result = 'ยี่' + thai_units[i % 8] + result
                elif (nums[i] == 1 and i == 1) or (nums[i] == 1 and i == 7):
                    result = thai_units[i % 8] + result
                elif nums[i] == 1 and i == 0 and len(nums) > 1:
                    result = 'เอ็ด'
                else:
                    result = thai_numbers[nums[i]] + thai_units[i % 8] + result
                
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.number_to_thai(101)
    print(f"Result: {result}")