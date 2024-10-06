class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def helper(currentsubset,index):
            if len(nums)==index:
                result.append(currentsubset[:])
                return
            helper(currentsubset,index+1)

            currentsubset.append(nums[index])

            helper(currentsubset,index+1)
            currentsubset.pop()
        helper([],0)

        return result
