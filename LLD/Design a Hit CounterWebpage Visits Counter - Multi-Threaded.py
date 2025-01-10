# https://codezym.com/question/6
Write code for low level design of a webpage visits counter.
There are n webpages in a website numbered 0 to n-1.
Hundreds of users visit webpages of this website simultaneously.
You have to record visit count for each page and return them when required.


class Solution:
    
    def init(self, total_pages, helper):
        self.helper = helper
        self.track = {}

        for i in range(total_pages+1):
            self.track[i] = 0
        
    def increment_visit_count(self, page_index):
        self.track[page_index] += 1

    def get_visit_count(self, page_index)-> int:
        return self.track[page_index]
