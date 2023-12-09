class Node:
    '''class Node reperesents an element of linked list'''
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
    
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_prev(self,value):
        if isinstance(value, Node) or not value:
            self.__prev = value
            return 
        else: raise ValueError(f"Node {value} doesn't exist")
    def set_next(self,value):
        if isinstance(value, Node) or not value:
            self.__next = value
            return
        else: raise ValueError(f"Node {value} doesn't exist")
 
    prev = property(get_prev, set_prev)
    next = property(get_next, set_next)
