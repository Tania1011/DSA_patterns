""" Middle of a Linked List
# Find the middle node of a linked list
# Example: input: 0 1 2 3 4
# Output: 2
# Explanation: If the number of nodes is even, then return the second middle node.
# input: 0 1 2 3 4 5
# Output: 3
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val
    
def build_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head



if __name__ == "__main__":
    values = list(map(int, input("Enter numbers: ").split()))
    head = build_list(values)
    result = middle_of_linked_list(head)
    print("Output:", result)
    

    
        