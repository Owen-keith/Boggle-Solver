import trie
import numpy as np

dictionary = trie.Trie()

file1 = open('BoggleSlvr/Dictionary.txt', 'r')
 
for line in file1:
    added = line.strip()
    if(len(added) > 2):
        dictionary.insert(added)
 
file1.close()

