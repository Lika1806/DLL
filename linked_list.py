import node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = node.Node(data, self.tail)
        if not self.head:
            self.head = new_node
            return
        if not self.tail:
            self.tail = new_node
            self.tail.prev = self.head
            self.head.next = self.tail
            return
        self.tail.next = new_node
        self.tail = new_node
        
    def prepend(self, data):
        new_node = node.Node(data, None, self.head)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = self.head.next
        
    def find_data(self,target_data):
        e = self.head
        while e:
            if e.data == target_data:
                return e
            e = e.next
        
    def insert_after(self, target_data,  data):
        target_node = self.find_data(target_data)
        if not target_node:
            raise ValueError ("Data doesn't exist")
        if target_node.next is None:
            self.append(data)
            return
        new_node = node.Node(data, target_node, target_node.next)
        target_node.next.prev = new_node
        target_node.next = new_node
            
    def insert_before(self, target_data, data):
        target_node = self.find_data(target_data)
        if not target_node:
            raise ValueError ("Data doesn't exist")
        if target_node.prev is None:
            self.prepend(data)
            return
        new_node = node.Node(data, target_node.prev, target_node)
        target_node.prev.next = new_node
        target_node.prev = new_node

    def delete(self, data):
        target_node = self.find_data(data)
        if not target_node:
            raise ValueError ("Data doesn't exist")
        if target_node.prev:
            target_node.prev.next = target_node.next
        if target_node.next:
            target_node.next.prev = target_node.prev

    def display(self):
        e = self.head
        if not e:
            return -1
        while e:
            print(e.data)
            e = e.next

    def is_empty(self) -> bool:
        return not bool(self.head)


