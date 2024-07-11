class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = [st for st in s]
        for i, st in enumerate(s):
            if st == '(':
                stack.append(i)
            elif st == ')':
                s[stack[-1]:i+1] = s[stack[-1]:i+1][::-1]
                stack.pop()
        finals = [st for st in s if st not in ['(', ')']]
        return ''.join(finals)