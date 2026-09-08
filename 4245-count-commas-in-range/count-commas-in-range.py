class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        else:
            # c=0
            # for i in range(1000,n+1):
            #     a = f"{i:,}"
            #     c += a.count(',')
            # return c
            if n<= 199999:
                return n-999