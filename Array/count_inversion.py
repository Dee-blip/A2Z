#https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array
class Solution:
    def merge_and_count(self,arr,temp,left,mid,right):
        i=left
        j=mid+1
        
        k=left
        inv_count=0
        
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp[k]=arr[i]
                i+=1
            else:
                temp[k]=arr[j]
                inv_count+=mid-i+1
                j+=1
            k+=1
        while i<=mid:
            temp[k]=arr[i]
            i+=1
            k+=1
        while j<=right:
            temp[k]=arr[j]
            j+=1
            k+=1
            
        for i in range(left,right+1):
            arr[i]=temp[i]
        return inv_count
    
    def merge_sort_and_count(self,arr,temp,left,right):
        inv_count=0
        if left<right:
            
            mid = (left+right)//2
            
            inv_count += self.merge_sort_and_count(arr,temp,left,mid)
            inv_count += self.merge_sort_and_count(arr,temp,mid+1,right)
            
            inv_count += self.merge_and_count(arr,temp,left,mid,right)
            
        return inv_count
    
    def inversionCount(self, arr):
        n=len(arr)
        temp = [0]*n
        return self.merge_sort_and_count(arr,temp,0,n-1)
