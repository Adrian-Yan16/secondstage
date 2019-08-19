class StackError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top = Node(val,self._top)

    def pop(self):
        if self._top is None:
            raise StackError("Empty")
        else:
            value = self._top.val
            self._top = self._top.next
            return value

    def top(self):
        if self._top is None:
            raise StackError("Empty")
        return self._top.val