class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for num in nums:
            tmp = currMax * num

            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp, currMin * num, num)
            res = max(res, currMax)
        return res