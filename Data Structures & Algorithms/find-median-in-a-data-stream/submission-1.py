class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        l,r = 0, len(self.arr) - 1
        median = 0
        while l<=r:
            if r - l == 1:
                if len(self.arr) % 2 == 0:
                    median = (self.arr[l] + self.arr[r]) / 2
            if l == r:
                if len(self.arr) % 2 != 0:
                    median = self.arr[r]
            l += 1
            r -= 1
        return median
                
