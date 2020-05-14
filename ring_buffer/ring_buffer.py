from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If storage.len is less than capacity
        if self.storage.length < self.capacity:
            # Add item to head of storage
            self.storage.add_to_head(item)

        # Else: If storage.len is equal than capacity
        else:
            # Remove from tail of storage
            self.storage.remove_from_tail()
            # Add item to head
            self.storage.add_to_head(item)

    def get(self):
        # If storage.length is 0
        if self.storage.length == 0:
            # Return
            return []

        # Else:
        else:
            # Create a list to save all the values
            my_list = []
            # Set current_node to storage.head
            current_node = self.storage.head

            # While current_node is not empty
            while current_node != None:
                # append current_node to storage
                my_list.append(current_node.value)
                # set current_node to current_node.next
                current_node = current_node.next

            # Return the list
            return my_list