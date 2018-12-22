
from htrie import Trie

x = Trie()
x.index_text('car','car')
x.index_text('cat','cat')
x.index_text('cart', 'cart')
x.index_text('cartoon', 'cartoon')
x.index_text('camera', 'camera')
x.index_text('cast','cast')
x.index_text('Batman', 'batman')
x.index_text('Baseline', 'baseline')
x.index_text('Bash', 'BasH')
print (x.prefix_match('car'))
print (x.prefix_match('as'))
print (x.pattern_match('as'))
print (x.pattern_match('car'))
print('Done')