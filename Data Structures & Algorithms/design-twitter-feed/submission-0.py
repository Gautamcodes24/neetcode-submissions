class Twitter:
    def __init__(self):
        self.user = [set() for _ in range(501)]
        self.tweets = []  # (tweetId, userId)

    def postTweet(self, userId, tweetId):
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId):
        ans = []
        for tweetId, author in reversed(self.tweets):
            if author == userId or author in self.user[userId]:
                ans.append(tweetId)
            if len(ans) == 10:
                break
        return ans

    def follow(self, followerId, followeeId):
        self.user[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.user[followerId].discard(followeeId)