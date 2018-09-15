#coding = utf-8
"""
[Difficulty : Medium]

Given a linked list, remove the n-th node
from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self):
        # init basic vars
        self.result = []

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # set dummy node
        dummy = ListNode(0)

        # set slow and fast node
        slow = fast = dummy

        # init fast node
        for _ in xrange(n):
            fast = fast.next

        # move nodes
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove wanted node
        slow.next = slow.next.next

        return dummy.next


    def test(self):
        
