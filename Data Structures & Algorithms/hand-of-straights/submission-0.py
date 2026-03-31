class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hashMap = {}
        for n in hand:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        minH = list(hashMap.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in hashMap:
                    return False
                
                hashMap[i] -= 1

                if hashMap[i] == 0:
                    if i != minH[0]:
                        return False 
                    heapq.heappop(minH)
        return True

