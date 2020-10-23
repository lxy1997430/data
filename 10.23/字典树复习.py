class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):#一层一层地插,而不是插在同一层
        node = self.root

        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data.get(char)
        node.is_word = True

    def search(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                return False
            node = node.data.get(char)
        return node.is_word

    def
