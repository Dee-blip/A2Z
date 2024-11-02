
class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        ans = []
        
        for q in indices:
            count = 0
            
            for i in range(q,N):
                if arr[i] > arr[q]:
                    count+=1
                    
            ans.append(count)
        
        return ans    
