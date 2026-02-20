class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return "#" in node
            ch = word[i]
            if ch == ".":
                return any(dfs(node[c], i+1) for c in node if c != "#")
            if ch not in node:
                return False
            return dfs(node[ch], i+1)
        return dfs(self.root, 0)
