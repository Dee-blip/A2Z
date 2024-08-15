class Solution:
	def search(self,pat, txt):
	    patd={}
	    for i in pat:
	        patd[i] = patd.get(i, 0) + 1
	    i=0
	    j=0
	    d={}
	    count=0
	    k =len(pat)
	    n=len(txt)
	    
	    while j<n:
	        if txt[j] in d:
	            d[txt[j]]+=1
	        else:
	            d[txt[j]]=1
	       
	        
	        if j-i+1<k:
	            j+=1
	        elif j-i+1==k:
	            if d==patd:
	                count+=1
	            d[txt[i]]-=1
	            if d[txt[i]] == 0:
                    del d[txt[i]]
	            i+=1
	            j+=1
	    return count
