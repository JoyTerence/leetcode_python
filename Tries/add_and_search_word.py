
class WordDictionary:

    def __init__(self):
        self.trie = {}
    
    def add_word(self, word):
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True
    
    def search_word(self, word):
        def search_in_trie(self, word, node):
            for index, ch in enumerate(word):
                if ch not in node:
                    if ch == ".":
                        for x in node:
                            if x != '$' and self.search_in_trie(word[index+1:], node[x]):
                                return True
                    return False
                node = node[ch]
            return '$' in node
        return search_in_trie(self, word, self.trie)