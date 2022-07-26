# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        q = deque([])
        if root: q.append(root)
            
        while q:
            maxVal = float("-inf")
            qLen = len(q)
            
            while qLen:
                node = q.popleft()
                maxVal = max(maxVal, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                qLen -= 1
            res.append(maxVal)
        
        return res