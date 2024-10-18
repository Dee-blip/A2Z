class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        arr=[]
        low = head
        high =head
        # length = 1
        while high.next is not None:
            # length+=1
            high = high.next
        
        while low!=high and low.data< high.data:
            current = low.data + high.data 
            if current == target:
                arr.append((low.data,high.data))
                low = low.next
                high = high.prev
            elif current > target:
                high = high.prev
            else:
                low =low.next
        return arr
