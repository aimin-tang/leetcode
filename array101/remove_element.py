from typing import List


class Solution:
    def get_next_val(self, nums: List[int], val: int, start: int, end: int):
        for i in range(start, end):
            if nums[i] == val:
                return i
        else:
            return end

    def get_last_non_val(self, nums: List[int], val: int, start: int, end: int):
        for i in range(end, start, -1):
            if nums[i] != val:
                return i
        else:
            return start

    def removeElement(self, nums: List[int], val: int) -> int:
        pass

nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
print(s.get_next_val(nums, 2, 0, 5))
print(s.get_last_non_val(nums, 2, 0, 5))
