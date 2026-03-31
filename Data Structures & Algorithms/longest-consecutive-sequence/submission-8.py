class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num = set(nums)

        for n in num:
            if n - 1 not in num:
                length = 1
                while (n + length) in num:
                    length += 1
                longest = max(length, longest)
        return longest
                

