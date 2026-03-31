class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force way
        # This has O(n^2)

        # res = 0
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         area = (r-l) * min(heights[l], heights[r])
        #         res = max(res, area)
        # return res

        # This has O(n)
        # optimal solution

        max_water = 0

        l,r = 0, len(heights)-1
        
        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            max_water = max(max_water, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_water 