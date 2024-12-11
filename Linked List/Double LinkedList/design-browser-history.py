class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        self.tail = self.current

    def visit(self, url: str) -> None:
        new_node = Node(url)

        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:

        while steps>0 and self.current.prev:
            self.current = self.current.prev
            steps-=1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps>0 and self.current.next:
            self.current = self.current.next
            steps-=1
        return self.current.url

browser_history = BrowserHistory("leetcode.com")
browser_history.visit("google.com")
browser_history.visit("facebook.com")
print(browser_history.back(1)) 
browser_history.visit("youtube.com")
print(browser_history.forward(1)) 

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
