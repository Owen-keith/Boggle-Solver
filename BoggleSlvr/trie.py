
class TrieNode:
 
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
 
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        #traverse the word character by character 
        for char in word:
            #check if the character is there in the list of children 
            if char in node.children:
                node = node.children[char]
            else:
                # else make a new TrieNode corresponding to that character 
                new_node = TrieNode(char)
                # add the new node to the list of children 
                node.children[char] = new_node
                node = new_node
        #after traversig the word set .is_end to true for the last #char
        node.is_end = True
    
    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
        for child in node.children.values():
            self.dfs(child, pre + node.char)
         
    def search(self, x):
        node = self.root
        self.output = []
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        #self.output = []
        self.dfs(node, x[:-1])
        return self.output