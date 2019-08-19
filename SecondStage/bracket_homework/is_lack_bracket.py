from SStack.SStack import *


class IsLackBracket:
    def __init__(self, text_):
        self._list = SStack()
        self.__text = text_

    def is_lack_bracket(self):
        i = 0
        while True:
            while i < len(self.__text):
                if self.__text[i] not in ("([{)]}"):
                    i += 1
                    break
                if self.__text[i] in ("([{"):
                    self._list.push(self.__text[i])
                    i += 1
                    break
                if self.__text[i] is ")" and self._list.top() is "(":
                    self._list.pop()
                elif self.__text[i] is "]" and self._list.top() is "[":
                    self._list.pop()
                elif self.__text[i] is "}" and self._list.top() is "{":
                    self._list.pop()
                elif self.__text[i] in (")]}"):
                    raise SStackError("%s不匹配" % self.__text[i])
                i += 1
            else:
                if self._list.is_empty():
                    raise SStackError("%s不匹配" % self._list.top())
                else:
                    print("匹配")


if __name__ == '__main__':
    test = "发布[A级0]名(员，每人)悬{万元，女[子瑶]在列。}"
    ilb1 = IsLackBracket(test)
    ilb1.is_lack_bracket()
