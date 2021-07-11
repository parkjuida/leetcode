from collections import defaultdict


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.comming = []

    def addNum(self, num: int) -> None:
        self.comming.append(num)

    def findMedian(self) -> float:
        self.comming.sort()
        comming_length = len(self.comming)
        if comming_length % 2 == 0:
            return (self.comming[(comming_length - 1) // 2] + self.comming[comming_length // 2]) / 2
        else:
            return self.comming[(comming_length - 1) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.findMedian()
mf.addNum(3)
mf.findMedian()
mf.addNum(2)
mf.findMedian()