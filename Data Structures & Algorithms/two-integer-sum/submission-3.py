class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        something = {}

        for i, n in enumerate(nums):
            curr = target - n
            if curr in something:
                return [something[curr], i]
            something[n] = i 
            