class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = collections.Counter(hand)
        for i in sorted(counter.keys()):
            while counter[i]>0:
                for j in range(i, i+groupSize):
                    if counter[j]<=0:
                        return False
                    counter[j] -=1
        return True