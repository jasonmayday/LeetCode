'''
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

示例：

输入：
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

输出：
    [null,null,null,null,false,true,true,true]

解释：
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

'''

class TrieNode:
    def __init__(self):                 # TrieNode 里面存储了两个信息：
        self.children = [None] * 26     # children 是该节点的所有子节点。
        self.isWord = False             # isWord 表示从根节点到当前节点为止，该路径是否形成了一个有效的字符串。

    def insert(self, word: str) -> None:
        node = self
        for ch in word:                 # 关键词放到「前缀树」时，需要把它拆成各个字符
            ch = ord(ch) - ord('a')     # 每个字符按照其在 'a' ~ 'z' 的序号
            if not node.children[ch]:
                node.children[ch] = TrieNode()  # 放在 chidren 对应的位置里面。
            node = node.children[ch]            # 下一个字符是当前字符的子节点。
        node.isWord = True


class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()      # 根节点不保存任何信息；

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)  # 将单词添加到字典树中即可。

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.isWord
            ch = word[index]
            if ch != '.':           # 待搜索的单词可能包含点号，因此在搜索过程中需要考虑点号的处理
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:                   # 如果当前字符是字母
                for child in node.children:     # 
                    if child is not None and dfs(index + 1, child): # 如果子结点存在则移动到子结点，继续搜索下一个字符
                        return True
            return False    # 如果子结点不存在则说明单词不存在，返回 false

        return dfs(0, self.trieRoot)
    
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))    # return False
    print(wordDictionary.search("bad"))    # return True
    print(wordDictionary.search(".ad"))    # return True
    print(wordDictionary.search("b.."))    # return True