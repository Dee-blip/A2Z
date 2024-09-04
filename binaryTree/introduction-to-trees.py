#https://www.geeksforgeeks.org/problems/introduction-to-trees/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-trees

class Solution:
    def countNodes(self, i):
        i-=1
        return 2**i
