class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashthing = defaultdict(list)

        for val in strs:
            count = [0] * 26
            for ch in val: 
                count[ord(ch) - ord('a')] += 1
            hashthing[tuple(count)].append(val)
        return list(hashthing.values())
