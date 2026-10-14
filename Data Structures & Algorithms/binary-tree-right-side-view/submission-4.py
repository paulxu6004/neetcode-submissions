# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root == None:
            return res


        q = [root]
        level = 0

        if root == None:
            return res
        
        while q:

            level = len(q)
            res.append(q[level - 1].val)
            
            for i in range(level):
                if q[0].left != None:
                    q.append(q[0].left)
                if q[0].right != None:
                    q.append(q[0].right)
                del q[0]

        return res
        

        