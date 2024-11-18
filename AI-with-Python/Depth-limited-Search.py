graph={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':[],
'G':[]
}
def DFS(graph,root_node,limit,goal_node=None):
    level=0
    frontier=[]
    expand=[]
    explore=[]
    current_node=root_node
    frontier.append((current_node,0))
    explore.append(current_node)
    while(frontier):
        current_node,level=frontier.pop()

        if current_node==goal_node:
            print("Goal reached")
            return explore
       
            
        if(level<=limit):
            if current_node not in explore:
             explore.append(current_node)  # Mark the current node as visited
            for child in reversed(graph[current_node]):
             print(f"child:{child}")
             if child not in  explore:
                frontier.append((child,level+1))


        expand.append(current_node)
    
        
    print("Goal not found")
    return explore


print(f"EXplored NOdes {DFS(graph, 'A',1,'G')}")
        
