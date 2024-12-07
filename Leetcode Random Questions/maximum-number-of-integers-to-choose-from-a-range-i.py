class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # n_array = [i for i in range(1,n+1)]

        # sum_threshold_check = 0
        # count = 0

        # for i in n_array:
        #     if i in banned:
        #         continue
        #     if sum_threshold_check + i <= maxSum:
        #         sum_threshold_check += i
        #         count+=1
        # return count

        banned_set = set(banned)
        sum_threshold_check = 0
        count = 0

        for i in range(1,n+1):
            if i in banned_set:
                continue
            if sum_threshold_check + i > maxSum: #optimized line
                break
            sum_threshold_check += i
            count+=1
        return count
