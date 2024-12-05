class Solution:
    def __init__(self):
        self.MAX_WIDTH = 0

    def get_final_word(self,i,j,eachWordSpace,extra_space,words):
        s=""
        for k in range(i,j):
            s+=words[k]
            #to skip another operation to prevent adding the extra space
            if k == j-1:
                continue
            s+= " " * eachWordSpace
            if extra_space > 0:
                s+=" "
                extra_space-=1


        while len(s)< self.MAX_WIDTH:
            s+=" "

        return s

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        n = len(words)
        self.MAX_WIDTH = maxWidth
        i = 0

        while i<n:
            letters_count = len(words[i])
            j = i+1
            space_slots = 0

            # Add words until we can't fit another without exceeding max_width

            while j < n and letters_count + space_slots + len(words[j]) + 1<= maxWidth:
                letters_count += len(words[j])
                space_slots += 1
                j+=1

            # Calculate remaining space for padding
            remaining_slots = maxWidth - letters_count

            eachWordSpace = 0 if space_slots==0 else remaining_slots // space_slots
            extra_space = 0 if space_slots==0 else remaining_slots % space_slots
            #For the last line of text, it should be left-justified, and no extra space is inserted between words.
            if j==n:
                eachWordSpace = 1
                extra_space = 0

            result.append(self.get_final_word(i,j,eachWordSpace,extra_space,words))
            i=j

        return result
        



            

        
