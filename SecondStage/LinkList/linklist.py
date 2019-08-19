class Node:
    def __init__(self,value,next = None):
        self.val = value
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self,list_):
        temp = self.head
        for item in list_:
            temp.next = Node(item)
            temp = temp.next

    def show(self):
        temp = self.head.next
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def is_empty(self):
        while self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    def head_insert(self,val):
        insert_node = Node(val)
        insert_node.next,self.head.next = self.head.next,insert_node

    def insert(self, index, val):
        temp = self.head
        for i in range(index):
            #超出链表范围，退出循环
            if temp.next is None:
                break
            temp = temp.next
        insert_node = Node(val)
        insert_node.next, temp.next = temp.next, insert_node

    def delete(self, val):
        temp = self.head
        while temp.next and temp.next.val != val:
            temp = temp.next
        if temp.next is None:
            raise ValueError("%d is not in linklist"%val)
        else:
            temp.next = temp.next.next

    def index(self,index):
        temp = self.head.next
        for i in range(index):
            if temp.next is None:
                raise IndexError("index is out of range")
            temp = temp.next
        return temp.val


class CombineLinklist:
    @staticmethod
    def combine_linklist(linklist1,linklist2):
        p = linklist1.head
        q = linklist2.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                temp = p.next
                p.next = q
                q = temp
                p = p.next
        p.next = q


ll1 = LinkList()
ll2 = LinkList()
list1 = [1,3,5,8,12,67]
list2 = [2,4,6.9,11]
ll1.init_list(list1)
ll2.init_list(list2)
c1 = CombineLinklist()
c1.combine_linklist(ll1,ll2)
ll1.show()




