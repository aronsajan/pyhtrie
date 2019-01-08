'''
trie_node.py: For storing data at each trie node
'''

__author__='Aron Sajan Philip'

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.node_data = []

    def add_data(self, data):
        self.node_data.append(data)
