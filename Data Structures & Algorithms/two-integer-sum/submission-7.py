class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashf = {}

        for i in range(len(nums)):
            lookfor = target - nums[i]
            if lookfor in hashf:
                    return [hashf[lookfor], i]
            
            hashf[nums[i]] = i

            