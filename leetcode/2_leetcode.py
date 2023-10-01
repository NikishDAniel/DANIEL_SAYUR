'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ListNode_to_List(root):
            lst = list()
            while root:
                lst.append(root.val)
                root = root.next
            return lst
        def List_to_ListNode(lst: list):
            root = None
            for x in lst:
                root = ListNode(x, root)
            return root
        first = ''.join([str(x) for x in ListNode_to_List(l1)])
        second = ''.join([str(x) for x in ListNode_to_List(l2)])
        returnn = str(int(first[::-1])+int(second[::-1]))
        return List_to_ListNode([int(x) for x in returnn])
