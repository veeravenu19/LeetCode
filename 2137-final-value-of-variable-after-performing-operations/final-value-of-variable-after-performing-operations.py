class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        c=0
        for i in operations:
            if i=="--X" or i=="X--":
                c-=1
            else:
                c+=1
        return c