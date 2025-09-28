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
    return []


def classify_edges(graph: GRAPH, trees: list[dict[str, list[int]]]) -> dict[str, set[tuple[str, str]]]:
    """
    Return a dictionary containing sets of each class of edges
    """
    classification = {
        'tree/forward': set(),
        'back': set(),
        'cross': set()
    }

    return classification


