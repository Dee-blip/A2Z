class Solution:
    def shortest_distance(self, matrix):
        V = len(matrix)

        distance = [[0] * V for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == -1:
                    distance[i][j] = float('inf')
                elif i == j:
                    distance[i][j] = 0
                else:
                    distance[i][j] = matrix[i][j]

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if distance[i][k] != float('inf') and distance[k][j] != float('inf'):
                        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        for i in range(V):
            for j in range(V):
                if distance[i][j] == float('inf'):
                    matrix[i][j] = -1  # Use -1 to indicate no path
                else:
                    matrix[i][j] = distance[i][j]

        return matrix
