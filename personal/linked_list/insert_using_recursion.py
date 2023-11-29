class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Creating nodes
node1 = ListNode(3)
node2 = ListNode(5)
node3 = ListNode(9)
node4 = ListNode(1)

# Connecting nodes to form a linked list: 3 -> 5 -> 9 -> 1 -> Null
node1.next = node2
node2.next = node3
node3.next = node4

def print_linked_list(node):
    current_node = node
    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next
    print("Null")

def insert_using_recursion(node1, val,index):
    if index == 0:
        new_node=ListNode(val)
        new_node.next=node1
        return new_node
    else:
        node1.next = insert_using_recursion(node1.next,val,index=index-1)
        return node1
    # return node1
# node1 = insert_using_recursion(node1,7,3)
# print_linked_list(node1)

