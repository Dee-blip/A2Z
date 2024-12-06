from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []

        ans_winner = []
        ans_loser = []

        for i,j in matches:
            winner.append(i)
            loser.append(j)

        dict_loser = {}
        for i in loser:
            dict_loser[i] = dict_loser.get(i,0)+1

        unique_winner = set(winner)
        for i in unique_winner:
            if dict_loser.get(i,0)== 0:
                ans_winner.append(i)
        
        for i,j in dict_loser.items():
            if j==1:
                ans_loser.append(i)
        
        ans_winner.sort()
        ans_loser.sort()

        return [ans_winner,ans_loser]
            
