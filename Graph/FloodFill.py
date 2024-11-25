class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])

        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(x,y):
            if x< 0 or x>=n or y<0 or y>=m or image[x][y]!=original_color:
                return
            image[x][y] = color

            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)


        dfs(sr,sc)

        return image
        
