class Solution:
    def makeFancyString(self, s: str) -> str:
        c=1
        an=s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                c=1
            if c<3:
                an+=s[i]
        return an