import networkx as nx
import pandas as pd

import config
from layoutgraph import initialize_graph, define_start_and_end_nodes
from locations import define_supply_locations, apply_supply_locations
from movement import find_first_shelf, find_nearest_neighbor

shortest_path = config.SHORTEST_PATH

def accumulate_distance(current_node, next_node, frequency):
    global total_distance
    total_distance += frequency * all_shortest_path_lengths[current_node][next_node]


# Data input
item_info_df = pd.read_excel('Current Supply Locations.xlsx', sheet_name='Supply Service Lines').dropna()
item_number_list = item_info_df['Item Number'].values.tolist()
service_line_dict = {int(row['Item Number']): row['Service Line'] for _, row in item_info_df.iterrows()}
pick_list_df = pd.read_excel('Pick List Data.xlsx', index_col='Pref ID Hash')
frequencies = pd.read_excel('Pick List Frequency.xlsx', index_col='Pref ID Hash')['count'].tolist()

# Define supply locations and apply to pick list dataframe
location_dict = define_supply_locations(item_number_list, service_line_dict)
pick_list_data = apply_supply_locations(pick_list_df, location_dict)

# Convert pick list dataframe to nested list
pick_lists = [list(set(filter(lambda x: x != 1000, pick_list))) for pick_list in pick_list_data]

G = initialize_graph()
start_node, end_node = define_start_and_end_nodes()

# Calculate shortest paths and lengths
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
all_shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

total_distance = 0

# Calculate total distance travelled
for pick_list, frequency in zip(pick_lists, frequencies):
    # Begin path at start_node
    path = [start_node]
    current_node = start_node
    # Find and move to designated first shelf if serpentine path
    if not shortest_path:
        nearest_shelf = find_first_shelf(pick_list)
        path.extend(all_shortest_paths[current_node][nearest_shelf][1:])
        accumulate_distance(current_node, nearest_shelf, frequency)
        current_node = nearest_shelf
        if current_node in pick_list:
            pick_list.remove(current_node)

    # Move to all other locations on pick list
    while pick_list:
        nearest_shelf = find_nearest_neighbor(current_node, pick_list, all_shortest_path_lengths)
        path.extend(all_shortest_paths[current_node][nearest_shelf][1:])
        accumulate_distance(current_node, nearest_shelf, frequency)
        current_node = nearest_shelf
        pick_list.remove(current_node)

    # Return to exit
    if current_node != end_node:
        path.extend(all_shortest_paths[current_node][end_node][1:])
        accumulate_distance(current_node, end_node, frequency)

daily_distance = total_distance / 260 / 5280
print(f'Average Daily Travel Distance: {round(daily_distance, 2)} mi')