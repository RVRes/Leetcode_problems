# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]


def to_listNode(l: list):
    ln = ListNode(l[0])
    head = ln
    for i in range(1, len(l)):
        ln.next = ListNode(l[i])
        ln = ln.next
    return head


def from_listNode(ln: ListNode):
    l_string = ''
    while ln:
        l_string += str(ln.val)
        ln = ln.next
    return l_string


# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     number_1 = int(''.join(map(str, list(reversed(list(l1))))))
#     number_2 = int(''.join(map(str, list(reversed(list(l2))))))
#     return list(reversed(str(number_1 + number_2)))


def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    l1_string = ''
    while l1:
        l1_string += str(l1.val)
        l1 = l1.next
    l2_string = ''
    while l2:
        l2_string += str(l2.val)
        l2 = l2.next
    result = str(int(l1_string[::-1]) + int(l2_string[::-1]))[::-1]
    head = ListNode(int(result[0]))
    ls_node = head
    for i in range(1, len(result)):
        ls_node.next = ListNode(int(result[i]))
        ls_node = ls_node.next
    return head


print(from_listNode(addTwoNumbers2(to_listNode(l1), to_listNode(l2))))
# print(addTwoNumbers2(l1, l2))
