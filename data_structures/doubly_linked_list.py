class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return str(self.data)
  
# Create and Handle list operations 
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None # Head of list 
    
    # Returns the linked list in display format 
    def __str__(self):
        node = self.head
        s = ""
        while node is not None:
            s += f"{node.data} "
            node = node.next
        return s

    # Pushes new data to the head of the list 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
  
    @staticmethod
    def convert_arr_to_dll(arr):
        ll = DoublyLinkedList()
        for i in arr[::-1]:
            ll.push(i)
        return ll

    def reverse(self):
        node = self.head
        while node is not None:
            next = node.next
            node.next, node.prev = node.prev, node.next
            prev = node
            node = next
        return prev
    
    def reverse_recursive(self, node):
        if node is None:
            return None
        node.next, node.prev = node.prev, node.next
        if node.prev is None:   # now previous, earlier next
            return node
        return self.reverse_recursive(node.prev)

    def swap_pair(self, node, prev=None):
        if node is None or node.next is None:
            prev.next = node
            return
        """
        make current2 the prior node and current1 the later
        prev.next = current2
        """
        current1, current2, next = node, node.next, node.next.next
        current2.prev, current2.next = prev, current1
        current1.prev = current2
        if prev is not None:
            prev.next = current2
        else:
            self.head = current2
        self.swap_pair(next, current1)
        return self.head


def test_dll():
    dll = DoublyLinkedList.convert_arr_to_dll([1,2,3,4,5,6,7, 8])
    print(dll)
    # dll.head = dll.reverse()
    # print(dll)
    # dll.head = dll.reverse_recursive(dll.head)
    # print(dll)
    dll.head = dll.swap_pair(dll.head)
    print(dll)


if __name__ == "__main__":
    test_dll()
