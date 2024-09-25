class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        MOD = 1000000007

        left =[0] *n
        right = [0] * n
        stack = []
        # calculate left
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]

            stack.append((arr[i],count))
            left[i] = count
        stack.clear()

        # calculate right
        for i in range(n-1,-1,-1):
            count = 1
            while stack and stack[-1][0]>=arr[i]:
                count += stack.pop()[1]

            stack.append((arr[i],count))
            right[i] = count

        total_sum=0
        for i in range(n):
            total_sum = (total_sum + left[i] * right[i] * arr[i]) % MOD
        return total_sum

        
