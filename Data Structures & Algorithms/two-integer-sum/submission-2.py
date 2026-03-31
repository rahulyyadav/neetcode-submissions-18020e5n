class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        something = {} #val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in something:
                return [something[diff], i]
            something[n] = i

