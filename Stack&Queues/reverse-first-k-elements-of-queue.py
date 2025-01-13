class Solution:
    def modifyQueue(self, q, k):
        temp = deque()
        
        for _ in range(k):
            if q:
                temp.append(q.popleft())

        while temp:
            q.append(temp.pop())
            
        for _ in range(len(q)-k):
            q.append(q.popleft())
            
        return q
