class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}
        
class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            if(char in node.children):
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode
        node.is_end = True
        
    def searchWordInTrie(self, x):
        
        node = self.root
        for char in x:
            if(char in node.children):
                node = node.children[char]
            else:
                return "Not Found"
        if(node.is_end):
            return "Found"
        else:
            return "Not Found"
        
    def findSuggestionsUtil(self,node,word):
        
        word = word + node.char
        
        if(node.is_end):
            self.output.append(word)
            return
        
        for child in node.children:
            self.findSuggestionsUtil(node.children[child],word)
            
        
    def findSuggestions(self, word):
        node = self.root
        found = True
        for char in word:
            if(char in node.children):
                node = node.children[char]
            else:
                found = False
                break
        self.output = []
        
        if(found):
            for child in node.children:
                self.findSuggestionsUtil(node.children[child],word)
        return self.output
    
        
                
t = Trie()
t.insert("was")
t.insert("word")
t.insert("war")
t.insert("what")
t.insert("where")
print(t.searchWordInTrie("wha"))

print(t.findSuggestions("w"))
            
