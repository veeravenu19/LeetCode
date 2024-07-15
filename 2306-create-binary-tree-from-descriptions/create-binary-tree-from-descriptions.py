# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        # Set to track nodes that are children
        child_nodes = set()

        # First pass: create nodes and establish parent-child relationships
        for desc in descriptions:
            parent_val, child_val, is_left = desc

            # Create parent node if it doesn't exist in the dictionary
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)

            # Create child node if it doesn't exist in the dictionary
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)

            # Establish the parent-child relationship
            if is_left:
                node_map[parent_val].left = node_map[child_val]
            else:
                node_map[parent_val].right = node_map[child_val]

            # Record the child node in the set
            child_nodes.add(child_val)

        # Second pass: identify the root node
        for desc in descriptions:
            parent_val = desc[0]
            # The root node is the one that is never a child node
            if parent_val not in child_nodes:
                return node_map[parent_val]

        return None
            