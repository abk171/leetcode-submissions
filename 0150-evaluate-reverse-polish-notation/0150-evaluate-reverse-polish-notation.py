class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: int(truediv(x,y))
        }
        st = []
        for v in tokens:

            if v in operators:
                y = st.pop()
                x = st.pop()
                st.append(operators[v](x,y))
            else:
                st.append(int(v))

        return st[0]
            
        