from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        even_q = deque([root])
        odd_q = deque()
        level = 0
        
        while even_q or odd_q:
            if level % 2 == 0:
                if not self.check_level(even_q, odd_q, True):
                    return False
            else:
                if not self.check_level(odd_q, even_q, False):
                    return False
            level += 1
            
        return True
    
    def check_level(self, curr_q, next_q, is_even_level):
        prev_val = None
        while curr_q:
            node = curr_q.popleft()
            if prev_val is not None:
                if (is_even_level and (node.val <= prev_val or node.val % 2 == 0)) or \
                   (not is_even_level and (node.val >= prev_val or node.val % 2 != 0)):
                    return False
            prev_val = node.val
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
        return True
