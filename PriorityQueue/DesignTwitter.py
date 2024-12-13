import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.trackPostTweet = defaultdict(list)
        self.trackFollowUnfollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp +=1
        self.trackPostTweet[userId].append([self.timestamp,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []

        self.trackFollowUnfollow[userId].add(userId)

        for followee_id in self.trackFollowUnfollow[userId]:
            if followee_id in self.trackPostTweet:
                values = self.trackPostTweet[followee_id]

                for i in range(len(values)):
                    max_heap.append([-values[i][0],values[i][1]])
        heapq.heapify(max_heap)

        ans=[]
        for _ in range(min(len(max_heap),10)):
            ans.append(heapq.heappop(max_heap)[1])
        return ans




    def follow(self, followerId: int, followeeId: int) -> None:
            self.trackFollowUnfollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.trackFollowUnfollow[followerId]:
            self.trackFollowUnfollow[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
