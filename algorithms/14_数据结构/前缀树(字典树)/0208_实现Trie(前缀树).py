"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree/comments/

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例：
    输入
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    输出
        [null, null, true, false, true, null, true]

    解释
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // 返回 True
        trie.search("app");     // 返回 False
        trie.startsWith("app"); // 返回 True
        trie.insert("app");
        trie.search("app");     // 返回 True

提示：
    1 <= word.length, prefix.length <= 2000
    word 和 prefix 仅由小写英文字母组成
    insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次

"""

class Trie:
    def __init__(self):             # 每个节点包含以下字段：
        self.children = [None] * 26 # 指向子节点的指针数组 children。对于本题而言，数组长度为 26，即小写英文字母的数量
        self.isEnd = False          # 布尔字段 isEnd，表示该节点是否为字符串的结尾。
    
    ''' 插入字符串 '''
    def insert(self, word: str) -> None:
        node = self
        for ch in word:                     # 关键词放到「前缀树」时，需要把它拆成各个字符
            ch = ord(ch) - ord("a")         # 每个字符按照其在 'a' ~ 'z' 的序号
            if not node.children[ch]:
                node.children[ch] = Trie()  # 放在 chidren 对应的位置里面。
            node = node.children[ch]        # 下一个字符是当前字符的子节点。
        node.isEnd = True                   # 一个输入字符串构建「前缀树」结束的时候，需要把该节点的 isWord 标记为 true，说明从根节点到当前节点的路径，构成了一个关键词。
    
    ''' 查找前缀 '''
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self                     # 从字典树的根开始，查找前缀
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:   # 子节点不存在。
                return None             # 说明字典树中不包含该前缀，返回空指针。
            node = node.children[ch]    # 子节点存在。沿着指针移动到子节点，继续搜索下一个字符。
        return node
    
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)          # 重复查找前缀，直到返回空指针或搜索完前缀的最后一个字符。
        return node is not None and node.isEnd  # 若搜索到了前缀的末尾，就说明字典树中存在该前缀。此外，若前缀末尾对应节点的 isEnd 为真，则说明字典树中存在该字符串。

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None    # 若搜索到了前缀的末尾，就说明字典树中存在该前缀。
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")    # 返回 True
    trie.search("app")      # 返回 False
    trie.startsWith("app")  # 返回 True
    trie.insert("app")
    trie.search("app")      # 返回 True