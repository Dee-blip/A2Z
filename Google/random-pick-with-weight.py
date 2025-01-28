import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_Sum = 0
        for weight in w:
            current_Sum += weight
            self.prefix_sum.append(current_Sum)
    
        self.totalWeight = current_Sum

    def pickIndex(self) -> int:

        random_weight = random.uniform(0, self.totalWeight)

        low , high = 0 , len(self.prefix_sum) - 1

        while low <= high:
            mid = (low+high)//2

            if self.prefix_sum[mid] > random_weight:
                high = mid - 1
            else:
                low = mid + 1
        return low #we need to return the smallest index

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
