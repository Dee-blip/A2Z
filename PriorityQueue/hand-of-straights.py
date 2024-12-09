import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False

        freq = Counter(hand)

        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for card in range(first, first+ groupSize):
                if card not in freq and freq[card]==0:
                    return False
                
                freq[card]-=1
                if freq[card]==0:
                    if card == min_heap[0]:
                        heapq.heappop(min_heap)
                    else:
                        del freq[card]

        return True


        
