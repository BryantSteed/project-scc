from scc import find_sccs, GRAPH

graph: GRAPH = {}

with open("court_data/Allcites.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    parts = line.split(" ")
    assert len(parts) == 2
    court_case = parts[0].strip()
    cited_case = parts[1].strip()
    if court_case not in graph:
        graph[court_case] = [cited_case]
    else:
        graph[court_case].append(cited_case)
    if cited_case not in graph:
        graph[cited_case] = []


sccs: list[set[str]] = find_sccs(graph)
edge_count = sum(len(adj) for adj in graph.values())
print(f"Graph has {len(graph)} nodes and {edge_count} edges")
density_factor = edge_count / len(graph)
print(f"Density factor: {density_factor:.6f}")
avg_scc_size = sum(len(scc) for scc in sccs) / len(sccs)
print(f"Found {len(sccs)} SCCs, average size {avg_scc_size:.2f}")
long_sccs = [scc for scc in sccs if len(scc) > 1]
print(f"Found {len(long_sccs)} non-trivial SCCs")
avg_nontrivial_scc_size = sum(len(scc) for scc in long_sccs) / len(long_sccs) if long_sccs else 0
print(f"Average non-trivial SCC size {avg_nontrivial_scc_size:.2f}")
largest_scc = max(sccs, key=len)
print(f"Largest SCC size {len(largest_scc)}")
print("Example largest SCC cases:", list(largest_scc))