class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def enqueue(self,val):
        self._elems.append(val)

    def dequeue(self):
        if self._elems is None:
            raise QueueError("Empty")
        del self._elems[0]

if __name__ == '__main__':
    queue1 = SQueue()
    list1 = [1,2,3,4,5]
    for item in list1:
        queue1.enqueue(item)
    queue1.dequeue()


