# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        def checkSame(roott,subroot):
            qu=deque([[roott,subroot]])
            while(qu):
                current,subCurr=qu.popleft()
                if not current and not subCurr:
                    continue
                if not current or not subCurr:
                    return False
                if current.val!=subCurr.val:
                    return False
                qu.append([current.left,subCurr.left])
                qu.append([current.right,subCurr.right])
            return True
        q=deque([root])
        # print(q)
        while(q):
            curr=q.popleft()
            if curr:
                if curr.val== subRoot.val and checkSame(curr,subRoot):
                    return True
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return False
                
