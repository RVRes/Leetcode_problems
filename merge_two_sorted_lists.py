# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_to_listnodes(self, input_list: list) -> ListNode or None:
        if not input_list:
            return None
        node = head = ListNode()
        for item in input_list:
            node.next = ListNode()
            node.next.val = item
            node = node.next
        return head.next

    def render_list_node(self, ln: ListNode):
        node = ln
        result_list = []
        while node:
            result_list.append(node.val)
            node = node.next
        return result_list

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            if not l1:
                node.next = l2
            elif not l2:
                node.next = l1
        return head.next


sol = Solution()
ln1 = sol.list_to_listnodes([1, 5, 10, 15])
ln2 = sol.list_to_listnodes([1, 7, 9, 13, 15, 17])
print(sol.render_list_node(sol.mergeTwoLists(ln1, ln2)))
