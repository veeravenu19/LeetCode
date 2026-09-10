# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def TreeTraversal(root,suma,count):
    if root:
        TreeTraversal(root.left,suma,count)
        suma+=root.val
        count+=1
        # print(root.val,suma,count, sep = " - ")
        TreeTraversal(root.right,suma,count)
    else:
        if count !=0:
            return suma//count
        else:
            return 0

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(root.left)
            right_sum, right_count, right_ans = dfs(root.right)

            suma = left_sum + right_sum + root.val
            count = left_count + right_count + 1

            ans = left_ans + right_ans

            if root.val == suma // count:
                ans += 1

            return suma, count, ans

        return dfs(root)[2]
