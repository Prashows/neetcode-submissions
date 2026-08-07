# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            
            qlen = len(queue)

            for data in range(qlen):
                right  = None
                node = queue.popleft()
                if node:
                    right = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if right:

                result.append(right.val)

        return result



