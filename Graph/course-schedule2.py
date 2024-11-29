class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        def dfs(node):
            if visited[node]==1: #1 is for visiting in recursion stack
                return False
            if visited[node]==2: #2 visited
                return True

            visited[node] = 1

            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False
            visited[node] =2
            stack.append(node)
            return True
       
        visited = [0]*numCourses
        stack = []

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []

        return stack[::-1]
