# Linked List Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
    
    def __repr__(self):
        return str(self.data)
  
# Create and Handle list operations 
class LinkedList: 
    def __init__(self): 
        self.head = None # Head of list 
    
    # Returns the linked list in display format 
    def __str__(self): 
        linkedListStr = "" 
        temp = self.head 
        while temp:
            linkedListStr = (linkedListStr + str(temp.data) + " ")
            temp = temp.next
        return linkedListStr
  
    # Pushes new data to the head of the list 
    def push(self, data): 
        temp = Node(data) 
        temp.next = self.head 
        self.head = temp
    
    @staticmethod
    def convert_arr_to_linked_list(arr):
        ll = LinkedList()
        for i in arr[::-1]:
            ll.push(i)
        return ll
  
    def reverse_normal(self, prev=None):
        # head = self.head
        while self.head.next:
            _next = self.head.next
            self.head.next = prev
            prev, self.head = self.head, _next
        self.head.next = prev
        return self.head
    
    def reverse_recursively(self):
        def reverse(current, prev=None):
            if current.next is None:
                self.head = current
                current.next = prev
                return
            reverse(current.next, current)
            current.next = prev
        reverse(self.head) if self.head is not None else None
        return self.head

    def swap_pairwise(self, prev=None):
        if self.head  is None or self.head.next is None:
            return self.head
        head = self.head
        current = head
        head = self.head.next
        while current is not None and current.next is not None:
            current1, current2 = current, current.next
            current1.next, current2.next = current2.next, current1
            if prev:
                prev.next = current2
            prev = current1
            current = current1.next
        return head

    def swap_n(self, n, prev=None):
        current = self.head
        head = current

        def check_if_reverse(current, n, i=1):
            while i < n and current is not None and current.next is not None:
                current = current.next
                i += 1

            if i == n:
                return True
            return False

        def reverse_n(current, n, prev=prev, i=1):
            first = current
            to_reverse = check_if_reverse(current, n)
            if not to_reverse:
                return first, None, None

            while current is not None and current.next is not None and i < n:
                next = current.next
                current.next = prev
                prev = current
                current = next
                i += 1
            next_club = current.next
            current.next = prev
            last = first
            first = current
            
            return first, last, next_club
        
        i = 0
        prev_last = None
        while True:
            first, last, next = reverse_n(current, n)
            if i == 0:
                head = first
            else:
                prev_last.next = first
            i += 1
            prev_last = last
            current = next

            if not last:
                break
            
        return head

    def check_if_sorted(self, current=None):
        if current is None or current.next is None:
            return True
        return self.check_if_sorted(current.next) and current.data >= current.next.data


def test_linked_list():
    linkedList = LinkedList.convert_arr_to_linked_list([5,6,3,2,1])
    print("Given linked list: ", linkedList) 

    # linkedList.head = linkedList.reverse_normal()
    # linkedList.head = linkedList.reverse_recursively()
    # print("Reversed linked list: ", linkedList)
    # linkedList.head = linkedList.swap_pairwise()
    # print("Pairwise Reversed linked list: ", linkedList)
    # linkedList.head = linkedList.swap_n(5)
    # print("N swapped linked list: ", linkedList)
    _sorted = linkedList.check_if_sorted(linkedList.head)
    print("Sorted: ", _sorted)

    

if __name__ == "__main__":
    test_linked_list()