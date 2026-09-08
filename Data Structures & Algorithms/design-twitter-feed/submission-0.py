class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.time, tweetId])
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId])- 1
                time, tweetid = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, [time, tweetid, followeeId, index -1])
        while minheap and len(res)< 10:
            time, tweetid, followeeId, index = heapq.heappop(minheap)
            res.append(tweetid)
            if index >=0:
                time , tweetid = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, [time,tweetid, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
