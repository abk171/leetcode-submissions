class node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key => node
        self.head = node(0,0)
        self.tail = node(0,0)

        self.head.next = self.tail
        self.tail.next = self.head

        self.tail.prev = self.head
        self.head.prev = self.tail        
    
    def remove(self, n):
        prev = n.prev
        next = n.next

        prev.next = next
        next.prev = prev
    
    def add_at_tail(self, n):
        prev = self.tail.prev

        prev.next = n
        n.next = self.tail
        self.tail.prev = n
        n.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.add_at_tail(n)
            return n.value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_n = node(key, value)
        self.add_at_tail(new_n)
        self.cache[key] = new_n

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)