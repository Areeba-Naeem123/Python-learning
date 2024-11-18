graph={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':[],
'G':[]
}
def DFS(graph,root_node,goal_node=None):

    frontier=[]
    expand=[]
    explore=[]
    current_node=root_node
    frontier.append(current_node)
    explore.append(current_node)
    while(frontier):
        current_node=frontier.pop()

        if current_node==goal_node:
            print("Goal reached")
            return explore
        if current_node not in explore:
            explore.append(current_node)  # Mark the current node as visited
            
    
        for child in reversed(graph[current_node]):
            print(f"child:{child}")
            if child not in  explore:
                frontier.append(child)

        expand.append(current_node)
    

    print("Goal not found")
    return explore


print(DFS(graph, 'A','G'))
        
