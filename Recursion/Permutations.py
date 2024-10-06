class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def generate_permutations(current,remaining):
            if not remaining:
                result.append(current)

            for i in range(len(remaining)):
                generate_permutations(current+[remaining[i]],remaining[:i]+remaining[i+1:])
            return result
        return generate_permutations([],nums)
