# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans=0
        q=deque([(root,root.val)])
        while(q):
            curr,path_max=q.popleft()
            if curr.val>=path_max:
                ans+=1
            if curr.left:
                q.append((curr.left,max(path_max,curr.val)))
            if curr.right:
                q.append((curr.right,max(path_max,curr.val)))
        return ans

