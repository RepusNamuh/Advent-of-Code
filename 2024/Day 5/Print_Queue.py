import math
from collections import defaultdict
import networkx as nx

with open("2024/Day 5/Print_Queue.txt") as f:
    q1 = defaultdict(set)
    rule1, updates = f.read().split("\n\n")
    rule1 = [list(map(int, line.split("|"))) for line in rule1.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates.splitlines()]
    

def part1(updates):
    global q1
    total = 0
    inOrder = True
    for update in updates:
        for i in range(len(update) - 1):
            current_index = q1.index(update[i])
            next_index = q1.index(update[i+1]) 
            if current_index > next_index:
                inOrder = False
                break

        if inOrder:
            total += update[math.floor(len(update)/2)]
    
    return total
