# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def find_small(node):
            nonlocal ans
            if not node:
                return
            find_small(node.left)
            ans.append(node.val)
            find_small(node.right)
            
        find_small(root)
        return ans[k-1]

