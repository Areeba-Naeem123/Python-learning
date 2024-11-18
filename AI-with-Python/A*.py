

import heapq  

graph = {
    '1': {'Child': {'2': 2, '3': 11, '4': 1}, 'h(n)': 8},
    '2': {'Child': {'5': 3}, 'h(n)': 7},
    '4': {'Child': {'3': 12, '6': 15}, 'h(n)': 11},
    '5': {'Child': {'3': 5, '7': 7}, 'h(n)': 5},
    '3': {'Child': {'2': 2, '7': 1, '6': 1}, 'h(n)': 0},
    '6': {'Child': {'7': 1}, 'h(n)': 1},
    '7': {'Child': {}, 'h(n)': 0} 
}

# A* Search Algorithm
def a_star(graph, start, goal):
    frontier = []
    explore=[]
    heapq.heappush(frontier, (graph[start]['h(n)'], start))  
    cost = {start: 0}  
    explore.append(current_node)

    
   
    while frontier:
        current_f, current_node = heapq.heappop(frontier)

        if current_node == goal:
          return True 
        
        if current_node not in explore:
            explore.append(current_node)  

        # Explore neighbors
        for neighbor, edge_cost in graph[current_node]['Child'].items():
            tentative_g = cost[current_node] + edge_cost  
            
            if neighbor not in cost or tentative_g < cost[neighbor]:
                cost[neighbor] = tentative_g
                f = tentative_g + graph[neighbor]['h(n)']  
                heapq.heappush(frontier, (f, neighbor))  
    
    return None 

# Running A* Search
start_node = '1'
goal_node = '5'
path = a_star(graph, start_node, goal_node)
print(f"Path from {start_node} to {goal_node}: {path}")
