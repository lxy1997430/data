#前缀树,trie树
#根节点不为kong
class TrieNode:#创建节点类
    def __init__(self):
        self.data = {}#存储下一级有什么内容
        self.is_word = False#判断是否为单词

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]#节点下移,屋子里有很多屋子,进入这间屋子
        node.is_word = True#插入了单词为true,没有为false,有几个就显示几个true

    def search(self,word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word #插入的时候设为了true

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True

t = Trie()
t.insert('love')
print(t.root)
print(t.search('lov'))
print(t.startsWith('l'))

