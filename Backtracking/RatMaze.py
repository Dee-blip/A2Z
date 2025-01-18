class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        n = len(mat)
        result = []

        def backtrack(x, y, path, visited):
            if x == n - 1 and y == n - 1:
                result.append("".join(path))
                return

            directions = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}

            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and mat[nx][ny] == 1:
                    visited[nx][ny] = True
                    path.append(direction)
                    backtrack(nx, ny, path, visited)

                    # Backtrack: undo the visit and the path choice
                    path.pop()
                    visited[nx][ny] = False

        if not mat or mat[0][0] == 0 or mat[n - 1][n - 1] == 0:
            return []

        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True

        backtrack(0, 0, [], visited)

        return result
