import pandas as pd
import networkx as nx

import config

layout = config.LAYOUT
shortest_path = config.SHORTEST_PATH

def read_edges():
    if shortest_path:
        edge_df = pd.read_excel(f'{layout} Shortest Graph Edges.xlsx')
    else:
        edge_df = pd.read_excel(f'{layout} Directed Graph Edges.xlsx')
    edge_list = [(row['Shelf 1'], row['Shelf 2'], row['Distance']) for _, row in edge_df.iterrows()]
    return edge_list

def initialize_graph():
    edge_list = read_edges()
    if shortest_path:
        G = nx.Graph()
    else:
        G = nx.DiGraph()
    G.add_weighted_edges_from(edge_list)
    return G

def define_start_and_end_nodes():
    if layout == 'Current Layout':
        return 49, 50
    if layout == 'Patterson Pope':
        return 117, 118