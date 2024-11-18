from collections import deque

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}

# for key , values in graph.items() :
#     print(f"node {key} has {values}")

def BFS(graph, root_node,goal_node):
    frontier=deque()
    expand_nodes=[]
    explored=[]

    current_node=root_node
    frontier.append(current_node)
    expand_nodes.append(current_node)
    explored.append(current_node)

    while(frontier):
        current_node=frontier.popleft()

        if current_node==goal_node:
            print(f"Goal found")
            return explored
        for child in graph[current_node]:  # Get neighbors of the current node
                print(f"child: {child}")
                if child not in explored:
                    frontier.append(child)
                    explored.append(child)

    
        # print(f"pop: {frontier.popleft()}") 
        expand_nodes.append(current_node)
        

    print("not found")
    return explored




print(BFS(graph, 'C','F'))


 

