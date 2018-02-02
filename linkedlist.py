from node import Node

class LinkedList:
    """LinkedList Data Structure."""

    def __init__(self):
        """LinkedList initialisation. """
        self.head = None

    def prepend(self, data):
        """Adding node before already existing node from lhs.
        Complexity is O(n)."""
        self.head = Node(data, self.head)

    def append(self, data):
        pass

    def insert(self, data, index):
        pass

    def remove(self, index):
        pass

    def __str__(self):
        """String representation of Single LinkedList.
        For Eg: 1 <- 2 <- 3. """
        current_node = self.head
        output = ''
        while current_node:
            output += '{}'.format(current_node.data)
            if current_node.next is not None:
                output += '<-'
            current_node = current_node.next
        return output


ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
print(ll)
