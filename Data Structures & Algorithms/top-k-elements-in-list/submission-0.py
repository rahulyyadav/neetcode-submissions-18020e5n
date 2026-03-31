class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        res = [] 

        most_common = count.most_common(k)

        for num, freq in most_common:
            res.append(num)
        return res