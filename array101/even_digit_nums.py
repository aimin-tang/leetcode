from typing import List

class Solutions:
    def num_of_digits(self, input: int) -> int:
        result = 0
        while input > 0:
            input = input // 10
            result += 1

        return result

    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            digits = 0
            while num > 0:
                num = num // 10
                digits += 1

            if digits % 2 == 0:
                result += 1

        return result

s = Solutions()
nums = [555,901,482,1771]
print(s.findNumbers(nums))
