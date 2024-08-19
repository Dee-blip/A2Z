  def longestKSubstr(self, s, k):
        i=0
        j=0
        n=len(s)
        max1=-1
        d={}
        #to print the string
        # start_index=0
        while j<n:
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            
            if len(d)>k:
                d[s[i]]-=1
                if d[s[i]]==0:
                    d.pop(s[i])
                i+=1
            elif len(d)==k:
                max1=max(max1,j-i+1)
                # start_index=i
            j+=1
        return max1 if max1>0 else -1
        # if max1==-1:
        #     return -1
        # else:
        #     return s[start_index:start_index+max1]
