from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        total_len: int = len(arr)
        i: int = 0
        while i < total_len - 1:
            if arr[i] != 0:
                i += 1
            else:
                arr[i:] = [0, 0] + arr[i + 1:total_len-1]
                i += 2


s = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
s.duplicateZeros(arr)
print(arr)
arr = [1, 2, 3]
s.duplicateZeros(arr)
print(arr)
arr = [0, 0, 0]
s.duplicateZeros(arr)
print(arr)
