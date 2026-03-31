class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxf = 0
        countS = {}

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            maxf = max(maxf, countS[s[r]])

            while (r - l + 1) - maxf > k:
                countS[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
