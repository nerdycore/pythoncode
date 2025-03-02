import heapq

def parse_graph(input_string):
    graph = {}
    lines = input_string.split("\n")
    for line in lines:
        node, edges = line.split(": ")
        neighbors = {}
        if edges.strip():
            for edge in edges.split(", "):
                neighbor, weight = edge.split(":")
                neighbors[neighbor.strip()] = float(weight)
        graph[node.strip()] = neighbors
    return graph

def dijkstra(graph, start):

    pq = [(0, start)]

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    paths = {node: [] for node in graph}
    paths[start] = [start]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                paths[neighbor] = paths[current_node] + [neighbor]
    
    return distances, paths

input_string = """A: B:3, C:3
B: A:3, D:3.5, E:2.8
C: A:3, E:2.8, F:3.5
D: B:3.5, E:3.1, G:10
E: B:2.8, C:2.8, D:3.1, G:7
F: G:2.5, C:3.5
G: F:2.5, E:7, D:10"""

graph = parse_graph(input_string)

start_node = "A"

distances, paths = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}:")
for node, distance in distances.items():
    print(f"  To {node}: {distance} (Path: {' -> '.join(paths[node])})")
