class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Creating nodes
nodea1 = ListNode(1)
nodea2 = ListNode(1)
nodea3 = ListNode(3)
nodea4 = ListNode(3)
nodea5 = ListNode(4)

# Connecting nodes to form a linked list: 3 -> 5 -> 9 -> 1 -> Null
nodea1.next = nodea2
nodea2.next = nodea3
nodea3.next = nodea4
nodea4.next = nodea5


# Creating nodes
nodeb1 = ListNode(1)
nodeb2 = ListNode(2)
nodeb3 = ListNode(2)
nodeb4 = ListNode(3)
nodeb5 = ListNode(5)

# Connecting nodes to form a linked list: 3 -> 5 -> 9 -> 1 -> Null
nodeb1.next = nodeb2
nodeb2.next = nodeb3
nodeb3.next = nodeb4
nodeb4.next = nodeb5


def print_linked_list(node):
    current_node = node
    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next
    print("Null")

def merge_two_list(a1,b1):
    h1=a1
    h2=b1
    node = None
    if h1.value < h2.value:
        head = h1
    else:
        head = h2
    while a1 != None and b1 != None:
        if a1.value<b1.value:
            node=a1
            a1 = a1.next
        else:
            node = b1
            b1 = b1.next
    while a1!=None:
        node = a1
        a1=a1.next
    while b1!= None:
        node = b1
        b1=b1.next

    return head


print_linked_list(merge_two_list(nodeb1,nodea1))