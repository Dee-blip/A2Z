class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.head= ListNode(0,0)
        self.tail= ListNode(0,0)
        self.head.next= self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key in self.cache:
            node= self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        node=ListNode(key,value)
        self.addNode(node)
        self.cache[key]=node

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.removeNode(lru_node)
            del self.cache[lru_node.key]

    def addNode(self,node):
        node.prev= self.head
        node.next = self.head.next
        self.head.next.prev= node
        self.head.next= node

    def removeNode(self,node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
