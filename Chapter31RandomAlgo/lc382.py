# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        res = self.head.val
        cur = self.head.next
        index = 1
        while cur:
            j = int(random.random() * (index + 1))
            if (j == 0):
                res = cur.val
            index += 1
            cur = cur.next
        return res
