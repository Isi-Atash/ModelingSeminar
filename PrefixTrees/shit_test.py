# Let's first define a TrieNode class to represent each node in the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

# Now let's create a Trie class to represent the whole trie
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number):
        node = self.root
        for digit in number:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.is_end_of_number = True
    
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        count = 1  # Count this node
        for child in node.children.values():
            count += self._count_nodes_recursive(child)
        return count

# Create a hypothetical list of phone numbers
phone_numbers = [
    "0123456789",
"1123456789"

]

# Create a trie and insert phone numbers
trie = Trie()
for number in phone_numbers:
    trie.insert(number)

# Count the number of nodes in the trie
node_count = trie.count_nodes()
print(node_count - 1)
