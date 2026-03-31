class TrieNodes:
    def __init__(self):
        self.node = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNodes()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.node:
                curr.node[c] = TrieNodes()
            curr = curr.node[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):

                c = word[i]

                if c == ".":
                    for child in curr.node.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.node:
                        return False
                    curr = curr.node[c]
            return curr.end
        return dfs(0, self.root)
