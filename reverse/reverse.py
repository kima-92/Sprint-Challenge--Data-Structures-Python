class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If self.head is empty or node is empty
        if self.head is None or node is None:
            # return 
            return

        # Else
        else:
            # Use recursion to call this function on the next node
            next_node = self.reverse_list(node.next_node, node)

            # If the next_node is None
            # This means it's the last node in this LL
            if next_node == None:
                # Set this node as the head
                self.head = node
                # Set the head's next node, as the previous node
                self.head.set_next(prev)
                # Return this node
                return node

            # Else: If the next_node is not None
            else:
                # Set the current node's next node, as the prev node
                node.set_next(prev)
                # Return this node
                return node
