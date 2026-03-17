from collections import defaultdict
from functools import cache

@cache
def get_ways_to_desired_node(node, target_node):
    if node == target_node:
        return 1
    return sum(get_ways_to_desired_node(neighbor, target_node) for neighbor in graph[node])

with open('real_input.txt') as file:
    data = file.read().split("\n")

graph = defaultdict(list)
for line in data:
    node, neighbors = line.split(":")
    graph[node] = neighbors.split(" ")[1:]

print(get_ways_to_desired_node("you", "out"))