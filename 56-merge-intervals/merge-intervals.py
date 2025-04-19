class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0], reverse=True)

        st = []
        st.append(intervals.pop())

        while intervals:
            start, end = intervals.pop()
            if st[-1][1] >= start:
                st_start, st_end = st.pop()
                if st_end > end:
                    st.append([st_start, st_end])
                else:
                    st.append([st_start, end]) 
            else:
                st.append([start, end])
            
        return st
                