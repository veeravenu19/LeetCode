class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = ['']
        for c in s:
            if c == '(': st += '',
            elif c == ')':
                v = st.pop()[::-1]
                st[-1] += v
            else: st[-1] += c
        return st.pop()