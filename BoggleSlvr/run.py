import trie
import utils
import numpy as np
from prerun import dictionary
from utils import *

char_bgl = ["S", "A", "U", "A", "T", "D", "E", "R", "H", "M", "A", "R", "T", "N", "A", "F", "F", "U", "E", "N", "P", "T", "R", "L", "B"]

graph = create_initial_graph(5)
found_words = trie.Trie()

for i in range(len(char_bgl)):
    boggle_search(graph, i, char_bgl, char_bgl[i], dictionary, found_words)

print(found_words.search(""))


