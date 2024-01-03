class ListNode:
    """Class to represent a node in a linked list.

    It has additional methods to build and render a linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def build_from_list(input_list: list) -> 'ListNode' or None:
        if not input_list:
            return None
        node = head = ListNode()
        for item in input_list:
            node.next = ListNode()
            node.next.val = item
            node = node.next
        return head.next

    @staticmethod
    def render_list_node(ln: 'ListNode'):
        node = ln
        result_list = []
        while node:
            result_list.append(node.val)
            node = node.next
        return result_list
