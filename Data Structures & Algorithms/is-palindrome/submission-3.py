class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = list("".join(char for char in s if char.isalnum()).lower())
        l, r = 0, len(compare) - 1

        while l < r:
            if compare[l] != compare[r]:
                return False
            l += 1
            r -= 1
        return True