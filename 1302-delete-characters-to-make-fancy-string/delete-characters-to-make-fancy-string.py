class Solution:
    def makeFancyString(self, s: str) -> str:
        i=0
        while(i<len(s)-2):
            if i+2<=len(s) and s[i]==s[i+1]==s[i+2]:
                s=s[0:i]+s[i+1:len(s)]
                i-=1
            i+=1
        # print(s)
        return s