from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])

nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))
