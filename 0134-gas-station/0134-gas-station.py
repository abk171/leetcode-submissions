class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        current_gas = 0
        start = 0
        
        for i , (g, c) in enumerate(zip(gas, cost)):
            total_gas += g - c
            current_gas += g - c
            
            if current_gas < 0:
                start = i + 1
                current_gas = 0
            
        return -1 if total_gas < 0 else start
                