class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        a=sum(chalk)
        if len(chalk)==1:
            return 0
        if s==k:
            return 0
        elif s<k:
            while s<=k:
                if s==k:
                    return 0
                else:
                    s+=a
            s-=(a)
            for i in range(len(chalk)):
                s+=chalk[i]
                if s>k:
                    return i
        else:
            # return 0
            s=0
            for i in range(len(chalk)):
                s+=chalk[i]
                if s>k:
                    return i