class SStackError(Exception):
    pass


class SStack:
    def __init__(self):
        self._elems = []

    def push(self, val):
        return self._elems.append(val)

    def pop(self):
        if self.is_empty():
            raise SStackError("SStack is empty")
        return self._elems.pop()

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise SStackError("Stack is empty")
        return self._elems[-1]

if __name__ == '__main__':
    stack1 = SStack()
    while True:
        temp = input()
        list1 = temp.split(" ")
        for se in list1:
            if se not in ("+", "-", "*", "/", "p"):
                stack1.push(se)
            elif se != "p":
                x = str(stack1.pop())
                y = str(stack1.pop())
                stack1.push(eval(y + se + x))
            else:
                re = stack1.top()
                print(re)
