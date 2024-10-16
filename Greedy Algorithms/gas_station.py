#https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        current_gas=0
        start_index=0

        for i in range(len(gas)):
            # total_gas+=gas[i]
            # total_cost+=cost[i]

            current_gas+=gas[i]-cost[i]

            if current_gas <0:
                start_index=i+1
                current_gas=0
        # what we have < what we need then we have to return -1 else print start_index
        if sum(gas)<sum(cost):
            return -1
        return start_inde

        
