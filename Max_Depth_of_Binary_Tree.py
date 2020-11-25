# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        levels = [[root]] #queue
        depth = 0
        
        while len(levels) != 0:         #or simply -> while levels:
            cur_level = levels.pop(0)
            next_level = []             #to appened to queue
            
            while len(cur_level) != 0:  #or simply -> while cur_level:
                cur_node = cur_level.pop(0)
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
            
            depth += 1
            
            if next_level != []:
                levels.append(next_level)
        
        return depth