class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [0, 0, 0]

        for t in triplets:
            if any(t[i] > target[i] for i in range(3)):
                continue

            for i in range(3):
                good[i] = max(good[i], t[i])
            
            if good == target:
                return True
        return False
