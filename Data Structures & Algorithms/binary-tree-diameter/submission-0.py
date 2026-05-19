# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx=0
        def ht(root):
            nonlocal maxx
            if not root:
                return 0
            left=ht(root.left)
            right=ht(root.right)
            maxx=max(maxx,left+right)
            return 1+max(left,right)
        _=ht(root)
        return maxx