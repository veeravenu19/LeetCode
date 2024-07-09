class Solution:
    def averageWaitingTime(self, l: List[List[int]]) -> float:
        ans = 0
        a = 0
        for i in range(len(l)):
            if i == 0:
                a = sum(l[i])
                ans += a-l[i][0]
            elif l[i][0]>=a:
                a = sum(l[i])
                ans += a-l[i][0]
            else:
                a = a+l[i][1]
                ans += a-l[i][0]
        return ans/len(l)