import dlb

class circleLL(dlb.DoublyLinkedBase):
    def __init__(self):
        self._header = dlb._Node(None, None, None)
        self._header._prev = self._header
        self._header._next = self._header
        self._size = 0
    def insert_first(self, a):
        dlb.DoublyLinkedBase._insert_between(self, a, self._header , self._header._next)
    def insert_last(self, a):
        dlb.DoublyLinkedBase._insert_between(self, a, self._header._prev, self._header)
    def delete_first(self):
        if dlb.DoublyLinkedBase.is_empty(self):
            raise DLB.Empty('List is empty')
        else:
            dlb.DoublyLinkedBase._delete_node(self, self._header._next)
    def delete_last(self):
        if dlb.DoublyLinkedBase.is_empty(self):
            raise DLB.Empty('List is empty')
        else:
            dlb.DoublyLinkedBase._delete_node(self, self._header._prev)
    def show(self):
        sl = ""
        if self._size == 0:
            return sl
        x = self._header._next
        while (x._element != None):
            sl += str(x._element) + " "
            x = x._next
        return sl
    
