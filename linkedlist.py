from node import Node

class LinkedList:
    """LinkedList Data Structure."""


    def __init__(self):
        """LinkedList initialisation."""
        self.head = None
        self.length = 0


    def __len__(self):
        return self.length


    def prepend(self, data):
        """Adding node at the start of LinkedList.
        Complexity is O(1)."""
        self.head = Node(data, self.head)
        self.length += 1


    def append(self, data):
        """Traverses throught the LinkedList and
        adds node at the end of LinkedList.
        Complexity is O(n)."""
        if self.head is None:
            self.prepend(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)
        self.length += 1


    def insert(self, data, index):
        """Insert a Node at index i. Complexity O(n)."""
        current_node = self.head
        counter = 0
        if self.length <= index:
            raise IndexError('Index out of range!!!')
        while current_node:
            prev_node = current_node
            current_node = current_node.next
            counter += 1
            if counter == index:
                current_node = Node(data, current_node)
                prev_node.next = current_node
                self.length += 1
                return


    def remove(self, index):
        """Remove a Node at index i. Complexity O(n)."""
        pass

    
    def search(self, data):
        """Search for node in LinkedList and return position.
        Complexity O(n)."""
        current_node = self.head
        counter = 0
        while current_node:
            if current_node.data == data:
                return counter
            current_node = current_node.next
            counter += 1
        return -1


    def __str__(self):
        """String representation of Single LinkedList.
        For Eg: 1 <- 2 <- 3."""
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
ll.prepend(50)
print(ll)
ll.insert(100, 1)
print(ll)

print("-"*20)

ll1 = LinkedList()
ll1.append(10)
ll1.append(20)
ll1.append(50)
print(ll1)
ll1.insert(100, 1)
print(ll1)

print("-"*20)

ll1 = LinkedList()
ll1.insert(100, 0)
print(ll1)

