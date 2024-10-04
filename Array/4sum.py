class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l= n-1
                temp= nums[i]+nums[j]
                while k<l:
                    temp1 = temp+ nums[k]+nums[l]
                    if temp1==target:
                        ans.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif temp1>target:
                        l-=1
                    else:
                        k+=1
        return list(ans)
                    

