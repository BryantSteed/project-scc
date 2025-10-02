import random
import sys
from time import time

GRAPH = dict[str, list[str]]
sys.setrecursionlimit(10000)


def prepost(graph: GRAPH) -> list[dict[str, list[int]]]:
    """
    Return a list of DFS trees.
    Each tree is a dict mapping each node label to a list of [pre, post] order numbers.
    The graph should be searched in order of the keys in the dictionary.
    """
    visited: set[str] = set()
    sort_func: callable = get_sort_func(graph)
    trees: list[dict[str, list[int]]] = []
    order_counter = 1
    for node in graph:
        if not node in visited:
            tree: dict[str, list[int]] = {}
            order_counter = explore_tree(graph, visited, sort_func, tree, node, order_counter)
            trees.append(tree)
    return trees

def explore_tree(graph, visited, sort_func, tree, node, order_counter):
    visited.add(node)
    tree[node] = [order_counter]
    order_counter += 1
    candidates = sorted(graph[node], key=sort_func)
    for candidate in candidates:
        if not candidate in visited:
            order_counter = explore_tree(graph, visited, sort_func, tree, candidate, order_counter)
    tree[node].append(order_counter)
    order_counter += 1
    return order_counter

def get_sort_func(graph: GRAPH):
    sort_dict: dict[str, int] = {}
    for i, node in enumerate(graph):
        sort_dict[node] = i
    def sorting_func(node: str):
        return sort_dict[node]
    return sorting_func


def find_sccs(graph: GRAPH) -> list[set[str]]:
    """
    Return a list of the strongly connected components in the graph.
    The list should be returned in order of sink-to-source
    """
    reverse_graph = get_reverse_graph(graph)
    prepost_trees = prepost(reverse_graph)
    node_order = get_node_order(prepost_trees)
    visited = set()
    sort_func = get_sort_func(graph)
    sccs = []
    for node in node_order:
        if not node in visited:
            scc = explore_primitive(graph, visited, sort_func, node, set())
            sccs.append(scc)
    return sccs

def explore_primitive(graph, visited, sort_func, node, scc):
    """Mine. all this does is explore all it can and returns everything
    that could be reached from the starting node. It doesnt worry about
    pre or post"""
    visited.add(node)
    scc.add(node)
    adjacents = sorted(graph[node], key = sort_func)
    for adjacent in adjacents:
        if not adjacent in visited:
            scc = explore_primitive(graph, visited, sort_func, adjacent, scc)
    return scc




def get_node_order(prepost_trees: list[dict[str, list[int]]]):
    node_post_orders: list[tuple[str, int]] = []
    for tree in prepost_trees:
        for node, orders in tree.items():
            node_post_orders.append((node, orders[1]))
    node_post_orders.sort(key = lambda t : t[1], reverse=True)
    node_order = [node_tuple[0] for node_tuple in node_post_orders]
    return node_order


def get_reverse_graph(graph: GRAPH):
    reverse_graph = {node : [] for node in graph}
    for from_node, to_nodes in graph.items():
        for to_node in to_nodes:
            reverse_graph[to_node].append(from_node)
    return reverse_graph


def classify_edges(graph: GRAPH, trees: list[dict[str, list[int]]]) -> dict[str, set[tuple[str, str]]]:
    """
    Return a dictionary containing sets of each class of edges
    """
    classification = {
        'tree/forward': set(),
        'back': set(),
        'cross': set()
    }
    for u, v in edge_iterator(graph):
        u_pre, u_post, v_pre, v_post = None, None, None, None
        for tree in trees:
            if u in tree:
                u_pre, u_post = tuple(tree[u])
            if v in tree:
                v_pre, v_post = tuple(tree[v])
        if u_pre < v_pre < v_post < u_post:
            classification['tree/forward'].add((u,v))
        elif v_pre < u_pre < u_post < v_post:
            classification['back'].add((u,v))
        else:
            classification['cross'].add((u,v))
    return classification

def edge_iterator(graph: GRAPH):
    for from_node, to_nodes in graph.items():
        for to_node in to_nodes:
            yield (from_node, to_node)
