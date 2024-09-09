#https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        arr3=[]

        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                arr3.append(nums1[i]) 
                i+=1  
            elif nums1[i]>=nums2[j]:
                arr3.append(nums2[j])
                j+=1

        while i<m:
            arr3.append(nums1[i])
            i+=1
        while j<n:
            arr3.append(nums2[j])
            j+=1
        
        for i in range(len(arr3)):
            nums1[i]=arr3[i]
