###############################
# Boggle Solver Util Functions#
# Owen C. Keith               #
# August 30, 2021             #
###############################


import trie
from trie import *
from prerun import dictionary
import numpy as np

def create_initial_graph(size):
    area = size**2
    blank = np.zeros((area, area))
    
    for j in range(area - size):
        blank[j, size+j] = 1
        blank[size+j, j] = 1

    counter = 0
    for i in range(area-1):
        if(counter%size != (size-1)):
            blank[i, i+1] = 1
            blank[i+1, i] = 1
        counter+=1

    counter2 = 0
    for k in range(area-size-1):
        if(counter2%size != (size-1)):
            blank[k, size+1+k] = 1
            blank[size+1+k, k] = 1
        counter2+=1

    counter3 = 0
    for h in range(area-size+1):
        if(counter3%size != 0):
            blank[h, size+h-1] = 1
            blank[size+h-1, h] = 1
        counter3+=1

    return blank

def remove_node(index, board_graph, size):
    board_graph2 = board_graph.copy()
    board_graph2[:, index] = np.zeros(size)
    board_graph2[index] = np.zeros(size)
    return board_graph2

def boggle_search(board_graph, index, char_array, partial_word, dictionary:Trie, found_dict:Trie):
    search = dictionary.search(partial_word)
    
    if(len(search) == 0):
        return found_dict
    
    if(search[0] == partial_word):
        found_dict.insert(partial_word)
    
    arr = list(board_graph[index,:])
    adj_list = [i for i, element in enumerate(arr) if element!=0]
    sub_board_graph = remove_node(index, board_graph, board_graph.shape[0])

    for j in range(len(adj_list)):
        new_word = partial_word + char_array[adj_list[j]]
        index = adj_list[j]
        found_dict = boggle_search(sub_board_graph, index, char_array, new_word, dictionary, found_dict)
    
    return found_dict















        

