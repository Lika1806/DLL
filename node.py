class Node:
    '''class Node reperesents an element of linked list'''
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
    
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, node):
        if node and not isinstance(node, Node):
            raise ValueError(f"Node {node} doesn't exist")
        self.__next = node
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, node):
        if node and not isinstance(node, Node):
            raise ValueError(f"Node {node} doesn't exist")
        self.__prev = node
    
