class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Creating nodes
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

# Connecting nodes to form a linked list: 3 -> 5 -> 9 -> 1 -> Null
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def print_linked_list(node):
    current_node = node
    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next
    print("Null")

print_linked_list(node1)

class Solution:
    def deleteDuplicates(self, head):
        node = head
        main = node
        while node.next != None:
            if node.next.value == node.value:
                node.next = node.next.next
            else:
                node = node.next
        return main

        



a=Solution()
print_linked_list(a.deleteDuplicates(node1))