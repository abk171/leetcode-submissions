from collections import namedtuple

temps = namedtuple('temps', ['index', 'temp'])

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0 for _ in range(len(temperatures))]
        
        for i, t in enumerate(temperatures):
            while st and t > st[-1].temp:
                result[st[-1].index] = i - st[-1].index
                st.pop()
            st.append(temps(i,t))
                
        return result