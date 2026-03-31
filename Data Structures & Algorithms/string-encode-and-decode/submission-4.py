class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            res = str(len(s)) + "#" + s
            enc = enc + res
        return enc
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res