class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # Dunder method for length
    def __len__(self):
        return self.size

    # Representation dunder
    def __repr__(self):
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)

    def enqueue(self, value):
        new_node = Node(value)
        # Check if queue is empty
        if self.rear is None:  # Same as self.front when queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        # Remove the front element if queue is not empty
        if self.front is None:
            raise IndexError('Queue is Empty')
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_value

    def peek(self):
        if self.front is None:
            raise IndexError('Queue is Empty')
        return self.front.value

    def is_Empty(self):
        return self.front is None

if __name__ == '__main__':
    q = Queue()

    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.enqueue(55)
    q.enqueue(66)

    print(q)            # Print all elements
    print(len(q))       # Print current queue size

    print(q.dequeue())  # Remove and print front
    print(q.dequeue())  # Remove and print next front

    print(q)            # Print updated queue
    print(len(q))       # Print updated size
