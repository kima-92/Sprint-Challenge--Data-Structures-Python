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
        pass