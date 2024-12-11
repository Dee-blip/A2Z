class Solution:
    def replaceWithRank(self, N, arr):
        #brute force approach is to sort the array using sorting function or algorithm and get
        # the index from the sorting by adding i+1 this is our answer- O(nlogn)
        
        
        #Priority Queue - this will also take same time complexity
        sorted_array = sorted(arr)
        
        d = {}
        rank = 1
        
        for i in range(len(sorted_array)):
            if sorted_array[i] not in d:
                d[sorted_array[i]] = rank
                rank+=1
        
        ans = [d[i] for i in arr]
        return ans
