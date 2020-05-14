from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current_node = None

    def append(self, item):

        # If current_node is None
        if self.current_node == None:
            # Set current_node to store the head of storage 
            self.current_node = self.storage.head

        # If storage.len is less than capacity
        if self.storage.length < self.capacity:
            # Add item to tail of storage
            self.storage.add_to_tail(item)
        
        # Else:
        else:
            # Replaze current_node's value with this item
            self.current_node.value = item
            # Set current_node to current_node.next
            # To save the next item in the next node
            self.current_node = self.current_node.next

    def get(self):
        # If storage.length is 0
        if self.storage.length == 0:
            # Return
            return []

        # Else:
        else:
            # Create a list to save all the values
            my_list = []
            # Set current to storage.head
            current = self.storage.head

            # While current is not empty
            while current != None:
                # append current to storage
                my_list.append(current.value)
                # set current to current.next
                current = current.next

            # Return the list
            return my_list