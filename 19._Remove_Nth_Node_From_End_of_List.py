# 19. Remove Nth Node From End of List
# Medium
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


from typing import Optional


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

    def removeNthFromEnd(
            self,
            head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        node = head
        list_node_copy = []
        while node:
            list_node_copy.append(node.val)
            node = node.next
        del list_node_copy[-n]
        head = None
        for item in list_node_copy:
            if not head:
                head = node = ListNode(item)
            else:
                node.next = ListNode(item)
                node = node.next
        return head

    def removeNthFromEnd_v2(
            self,
            head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        count = 0
        fast = slow = head
        while count < n:
            count += 1
            fast = fast.next
        # deletes head
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        # n=1 deletes last element - no need to link the tail
        slow.next = slow.next.next if n != 1 else None

        return head


if __name__ == '__main__':
    N = 1
    sol = Solution()
    ln1 = sol.list_to_listnodes([1, 7, 9, 13, 15, 17])
    result = sol.removeNthFromEnd(ln1, N)
    print(sol.render_list_node(ln1))
    print(sol.render_list_node(result))
    result = sol.removeNthFromEnd_v2(ln1, N)
    print(sol.render_list_node(result))
