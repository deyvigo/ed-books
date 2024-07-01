class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.is_end_of_word = False
    self.full_words = {}

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.is_end_of_word = True
    node.full_words[word] = True

  def _search_prefix(self, prefix: str) -> TrieNode:
    node = self.root
    for char in prefix:
        if char not in node.children:
            return None
        node = node.children[char]
    return node
  
  def search(self, prefix):
    node = self._search_prefix(prefix)
    if not node:
      return []
    
    results = []
    self._collect_all_words(node, results)
    return results
  
  def _collect_all_words(self, node, results):
    results.extend(node.full_words)
    for char, next_node in node.children.items():
      self._collect_all_words(next_node, results)