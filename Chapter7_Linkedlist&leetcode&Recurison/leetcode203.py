# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 1 - 时间复杂度: O(N)- 空间复杂度: O(1)
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        prev = head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head

    # 2- 时间复杂度: O(N)- 空间复杂度: O(1)
    class Solution:
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """
            if not head:
                return head
            head.next = self.removeElements(head.next, val)
            return head if head.val != val else head.next

        # 3- 时间复杂度: O(N)- 空间复杂度: O(1)

    class Solution:
        def removeElements(self, head, val):
            """
            :type head: ListNode
            :type val: int
            :rtype: ListNode
            """
            if not head:
                return head
            res = self.removeElements(head.next, val)
            if head.val == val:
                return res
            else:
                head.next = res
                return head