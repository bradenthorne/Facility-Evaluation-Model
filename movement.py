import config

layout = config.LAYOUT

def find_first_shelf(pick_list):
    minimum_index = min(pick_list)
    if layout == 'Current Layout':
        if minimum_index in range(0, 18):
            return 0
        if minimum_index in range(18, 32):
            return 18
        if minimum_index in range(32, 49):
            return 32
        else:
            return minimum_index
    if layout == 'Patterson Pope':
        if minimum_index in range(0, 8):
            return 0
        if minimum_index in range(8, 16):
            return 14
        if minimum_index in range(16, 24):
            return 16
        if minimum_index in range(24, 33):
            return 31
        if minimum_index in range(33, 43):
            return 33
        if minimum_index in range(43, 55):
            return 53
        if minimum_index in range(55, 61):
            return 55
        if minimum_index in range(61, 73):
            return 72
        if minimum_index in range(73, 99):
            return 73
        if minimum_index in range(99, 113):
            return 112
        else:
            return minimum_index

def find_nearest_neighbor(current_node, nodes, all_path_lengths):
    # Find the closest node that is not the current node itself
    nearest_node = None
    min_distance = float('inf')
    for node in nodes:
        if node != current_node and all_path_lengths[current_node][node] < min_distance:
            nearest_node = node
            min_distance = all_path_lengths[current_node][node]
    return nearest_node
