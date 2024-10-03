
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        sorted_jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        # max_deadline = max(job.deadline for job in Jobs)

        
        job_sequence = [-1]*n
        
        jobs_done=0
        max_profit= 0 
        
        for job in sorted_jobs:
            for j in range(min(n,job.deadline)-1,-1,-1):
                if  job_sequence[j]== -1:
                    job_sequence[j] = job.id
                    jobs_done+=1
                    max_profit+= job.profit
                    break
        return [jobs_done,max_profit]
        
