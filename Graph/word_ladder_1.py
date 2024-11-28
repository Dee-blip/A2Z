from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0 
        
        queue = deque([(beginWord,1)])

        while queue:
            current_word,steps = queue.popleft()

            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    transformed_word = current_word[:i] + c + current_word[i+1:]

                    if transformed_word == endWord:
                        return steps+1
                    
                    if transformed_word in wordList:
                        queue.append((transformed_word,steps+1))
                        wordList.remove(transformed_word)
        return 0

        
