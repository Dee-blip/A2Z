#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Optimised Approach
        n1, n2 = len(nums1), len(nums2)
        total_len = n1 + n2

        index1 = (total_len - 1) // 2  
        index2 = total_len // 2        

        i, j = 0, 0
        merged_count = 0
        median1, median2 = 0, 0

        while i < n1 or j < n2:
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                current_val = nums1[i]
                i += 1
            else:
                current_val = nums2[j]
                j += 1
            
            if merged_count == index1:
                median1 = current_val
            if merged_count == index2:
                median2 = current_val
                break  
            
            merged_count += 1

        if total_len % 2 == 1:
            return float(median2)  
        else:
            return (median1 + median2) / 2 



        # Brute Force Approach
        # merged = sorted(nums1 + nums2)

        # total_len = len(merged)
        
        # if total_len % 2 == 1:
        #     return merged[math.floor(total_len // 2)]
        # else:
        #     return (merged[math.floor((total_len/2)-1)]+merged[math.floor(((total_len+2)/2)-1)])/2


        


        
