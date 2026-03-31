class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            nrob = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = nrob
        return rob2
