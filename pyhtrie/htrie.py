
'''
htrie.py : Trie data-structure used for faster accessing of keyword data.
'''

__author__ = 'Aron Sajan Philip'

from trie_node import TrieNode

class Trie(object):
    def __init__(self):
        self.root_nodes = {}
        self.node_map = {}

    def index_text(self, keyword, data):
        self.add_text_nodes(self.root_nodes, keyword, data)


    def add_text_nodes(self, node_children, text, data):
        if len(text) > 0:
            if text[0] in node_children:
                target_node = node_children[text[0]]
                if len(text)>1:
                    self.add_text_nodes(target_node.children, text[1:])
                else:
                    target_node.add_data(data)
            else:
                new_node = TrieNode()
                new_node.add_data(data)
                if text[0] in self.node_map:
                    self.node_map[text[0]].append(new_node)
                else:
                    self.node_map[text[0]] = []
                    self.node_map[text[0]].append(new_node)
                node_children[text[0]] = new_node

    def prefix_match(self, prefix_text):
        start_node = traverse_to_node(self.root_nodes, prefix_text)
        return child_data_collect(start_node)

    def pattern_match(self, pattern_text):
        collected_data = []
        if len(pattern_text)>0:
            if pattern_text[0] in self.node_map:
                starting_node_list = self.node_map[pattern_text[0]]
                for starting_node in starting_node_list:
                    target_node = traverse_to_node(starting_node,pattern_text)
                    data_fetched = child_data_collect(target_node)
                    if data_fetched:
                        collected_data = collected_data + data_fetched
        return collected_data

def traverse_to_node(from_node_map, keyword):
    if len(keyword)>0:
        if keyword[0] in from_node_map:
            target_node = from_node_map[keyword[0]]
            if len(keyword)>1:
                return traverse_to_node(target_node.children, keyword[1:])
            return target_node
    return None


def child_data_collect(trie_node):
    if trie_node:
        collected_data = trie_node.node_data
        for key, child_node in trie_node.children.items():
            collected_data = collected_data + child_data_collect(child_node)
        return collected_data
    else:
        return []







