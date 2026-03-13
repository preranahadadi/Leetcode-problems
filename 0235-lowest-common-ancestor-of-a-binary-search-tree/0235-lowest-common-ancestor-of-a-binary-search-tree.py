# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
        #condition to check if the tree is present in the right 
            if root.val < p.val and root.val < q.val:
                root=root.right
        #condition to check if the tree is present in the left
            elif root.val > p.val and root.val > q.val:
                root= root.left
        # if from the root it diverges then root is the answer
            else:
                return root
        

        