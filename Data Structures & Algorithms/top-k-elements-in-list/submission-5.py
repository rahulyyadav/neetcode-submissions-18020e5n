class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for num, v in hashmap.items():
            freqs[v].append(num)
        result = []
        for n in range(len(freqs) - 1, 0, -1):
            for i in freqs[n]:
                result.append(i)
                if len(result) == k:
                    return result
        

