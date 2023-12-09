class Node:
    '''class Node reperesents an element of linked list'''
    def __init__(self, data, prev_node=None, next_node=None):
        self.__data = data
        self.__prev = prev_node
        self.__next = next_node
    
    def get_data(self):
        return self.__data
    def get_prev(self):
        return self.__prev
    def get_next(self):
        return self.__next
    def set_data(self,value):
        self.__data = value
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
 
    data = property(get_data, set_data)
    prev = property(get_prev, set_prev)
    next = property(get_next, set_next)
