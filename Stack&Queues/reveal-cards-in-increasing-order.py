#https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        ans = [0] * n

        q = deque(range(len(deck)))


        for n in deck:
            i = q.popleft()
            # print(q)
            ans[i] = n
            #rotate the next index or put the next card into end of the q
            if q:
                q.append(q.popleft())
            # print(q)
        return ans
        
