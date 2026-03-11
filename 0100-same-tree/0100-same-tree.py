# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both the trees are not present then true
        if not p and not q:
            return True 
        #if either tree is not present
        if not p or not q:
            return False
        # If both the values are not equal
        if p.val != q.val:
            return False
        # Case when both right and left values are same 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        