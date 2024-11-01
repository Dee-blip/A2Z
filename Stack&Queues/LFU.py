from collections import defaultdict
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1 # initialize the node with the starting frequency one
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size +=1

    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1

    def remove_last(self):
        if self.size>0:
            node = self.tail.prev
            self.remove_node(node)
            return node
        return None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0 # track the min frequency among the keys currently in the cache. So when cache is fulled  we can see which node has LF for eviction.
        self.cache = {} #stores the actual key-value entries in the cache, where each key maps to a Node object containing the value, frequency, and pointers for efficient traversal.
        self.freq_map = defaultdict(DoublyLinkedList) 
        self.size = 0

    def update_freq(self,node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        #if suppose after deletion of the 1:node from freq_map, if there 2 freq_map exists then we have to shift our min_freq to 2.
        if self.freq_map[freq].size== 0 and freq == self.min_freq:
            self.min_freq+=1

        node.freq+=1
        self.freq_map[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update_freq(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_freq(node)  # on each case we have to update the freq as we accessing the ele in both the case
        else:
            if self.size == self.capacity:
                remove = self.freq_map[self.min_freq].remove_last() #our dll ordered by the recency and least recent always at the back of the DLL.
                del self.cache[remove.key]
                self.size-=1
            
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size+=1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
