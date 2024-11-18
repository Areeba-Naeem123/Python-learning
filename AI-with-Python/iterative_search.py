graph={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':[],
'G':[]
}

def IDDS(graph,root_node,goal_node,max_depth):
    for limit in range(max_depth + 1):
        print(f"searching at depth {limit}")
        if DFS(graph, 'A',limit,'G'):
           print("Goal found")
           return True
        
    print("Goal not found within max depth")










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
            print(explore)
            return True
       
            
        if(level<limit):
            if current_node not in explore:
             explore.append(current_node)  
            for child in reversed(graph[current_node]):
             print(f"child:{child}")
             if child not in  explore:
                frontier.append((child,level+1))


        expand.append(current_node)
    
    print(explore)
    print("Goal not found")
    return False


IDDS(graph,'A','G',1)        
