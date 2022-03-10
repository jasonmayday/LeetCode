"""
https://leetcode-cn.com/problems/design-twitter/

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。

实现 Twitter 类：
    Twitter() 初始化简易版推特对象
    void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。
    List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
    void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。
    void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。

示例：
    输入
        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    输出
        [null, null, [5], null, null, [6, 5], null, [5]]

    解释
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
        twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
        twitter.follow(1, 2);    // 用户 1 关注了用户 2
        twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
        twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
        twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
        twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2

提示：
    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 10^4
    所有推特的 ID 都互不相同
    postTweet、getNewsFeed、follow 和 unfollow 方法最多调用 3 * 10^4 次

"""
from typing import List

"""方法一：哈希表 + 链表"""
class Twitter:
    def __init__(self):
        self.users = dict() # key: value分别对应用户 userId(int) 和 其关注者(list)
        self.posts = []     # 发布的帖子，每个元素格式为 [userId, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None: # 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId
        self.posts.append([userId, tweetId])    # 将帖子加入 posts 列表
        if not self.users.get(userId):          # 同步更新用户列表，如果 userId 在字典中的值不存在，则设为初始值 [],否则不操作
            self.users[userId] = []

    def getNewsFeed(self, userId: int) -> List[int]:
        # 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
        if userId not in self.users.keys():  # 检查 userId 的合法性,如果该用户不存在，直接返回
            return
        else:  # 用户存在
            ids = [userId] + self.users.get(userId)  # 计算待排查id，包括用户自身 id 还有他 follow 的人的 id
            tmp = []  # 待返回的结果集
            count = 10  # 计数器：排查最新的10条
            for post in self.posts[-1:-(len(self.posts) + 1):-1]:  # 开始排查，并将 tweetId 加入结果集
                if count > 0:
                    if post[0] in ids:
                        tmp.append(post[1])
                        count -= 1
            return tmp

    def follow(self, followerId: int, followeeId: int) -> None:     # ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。
        if followerId not in self.users.keys():  # 检查 followerId 用户的 id 合法性，如果没在 self.users 中出现过，则设为初始值
            self.users[followerId] = []
            self.users[followerId].append(followeeId)
        else:  # followerId 如果在 self.users 中出现过，则直接将 followeeId 直接加入
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:   # ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。
        if followerId not in self.users.keys():  # 检查合法性，如果 followerId 未曾出现，则直接返回
            return
        else:
            if followeeId in self.users[followerId]:  # 检查被移除的 id 的合法性，如果存在直接删除
                self.users[followerId].remove(followeeId)
            else:  # 被移除的 id 不存在，返回
                return

if __name__ == "__main__":
    twitter = Twitter()
    print(twitter.postTweet(1, 5))     # None   | 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
    print(twitter.getNewsFeed(1))      # [5]    | 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
    print(twitter.follow(1, 2))        # None   | 用户 1 关注了用户 2
    print(twitter.postTweet(2, 6))     # None   | 用户 2 发送了一个新推文 (推文 id = 6)
    print(twitter.getNewsFeed(1))      # [6, 5] | 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
    print(twitter.unfollow(1, 2))      # None   | 用户 1 取消关注了用户 2
    print(twitter.getNewsFeed(1))      # [5]    | 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2
