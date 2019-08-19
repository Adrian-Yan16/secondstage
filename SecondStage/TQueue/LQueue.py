class QueueError(Exception):
    pass


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LQueue:
    def __init__(self):
        self._rear = self._head = Node(None)

    def is_empty(self):
        return self._head == self._rear

    def enqueue(self,val):
        self._rear.next = Node(val)
        self._rear = self._rear.next

    def dequeue(self):
        if self._head == self._rear:
            raise QueueError("Empty")
        self._head = self._head.next
        return self._head.val


if __name__ == '__main__':
    lq1 = LQueue()
    lq1.enqueue(1)
    lq1.enqueue(2)
    lq1.enqueue(3)
    print(lq1.dequeue())
    print(lq1.dequeue())
    print(lq1.dequeue())
