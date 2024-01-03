# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional
from _list_nodes_helper import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2
        head = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 else list2
        return head.next


if __name__ == '__main__':
    ln1 = ListNode.build_from_list([2, 3])
    ln2 = ListNode.build_from_list([4, 5, 7, 15])
    print(ListNode.render_list_node(ln1))
    print(ListNode.render_list_node(ln2))
    sol = Solution()
    result = sol.mergeTwoLists(ln1, ln2)
    print(ListNode.render_list_node(result))

