class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        remainder=k%s
        cu=0
        for i in range(len(chalk)):
            cu+=chalk[i]
            if cu>remainder:
                return i