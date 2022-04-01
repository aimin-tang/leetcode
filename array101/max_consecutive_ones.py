from typing import List


class Solution:
    def longestFrom(self, nums: List[int], pos: int) -> int:
        """
        return position of last 1, when we start at pos.
        """
        if nums[pos] != 1:
            raise RuntimeError('Unexpected usage to start from non-1.')

        for i in range(pos + 1, len(nums)):
            if nums[i] == 0:
                return i - 1
        else:
            return len(nums) - 1

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result: int = 0
        start: int = 0

        while start < len(nums):
            if nums[start] == 1:
                cur_result = self.longestFrom(nums, start)
                if cur_result - start + 1 > result:
                    result = cur_result - start + 1
                start = cur_result + 1
            else:
                start += 1

        return result


nums = [1, 0]
test1 = Solution()
# print(test1.longestFrom(nums, 0))
print(test1.findMaxConsecutiveOnes([1, 0]))
