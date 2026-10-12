class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashf = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashf:
                return [hashf[needed], i]
            hashf[nums[i]] = i
        