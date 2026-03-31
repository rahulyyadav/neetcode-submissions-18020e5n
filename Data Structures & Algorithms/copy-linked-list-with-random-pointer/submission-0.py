"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        New = {None: None}

        p = head

        while p:
            copy = Node(p.val)
            New[p] = copy
            p = p.next
        
        p = head

        while p:
            copy = New[p]
            copy.next = New[p.next]
            copy.random = New[p.random]
            p = p.next
        
        return New[head]