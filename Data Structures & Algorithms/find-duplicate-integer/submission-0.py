class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasmap = set()

        for num in nums:
            if num in hasmap:
                return num
            hasmap.add(num)
        return -1