#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        activities = [(start[i],end[i],i+1) for i in range(n)]
        
        activities.sort(key=lambda x:x[1])
        

        count=1
        
        end_time = activities[0][1]
        
        for i in range(1,n):
            if activities[i][0] > end_time:
                count+=1
                end_time =activities[i][1]
        return count
