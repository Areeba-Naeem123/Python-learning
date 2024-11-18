

import heapq  

graph={
'1':{'Child':['2','3','4'],'h(n)':8},
'2':{'Child':['5'],'h(n)':7},
'4':{'Child':['3','6'],'h(n)':11},
'5':{'Child':['3','7'],'h(n)':5},
'3':{'Child':['2','7','6'],'h(n)':0},
'6':{'Child':['7'],'h(n)':1},
'7':{'Child':[],'h(n)':0}
}
def Best_FS(graph,root_node,goal_node=None):

    frontier=[]
    expand=[]
    explore=[]
    current_node=root_node
    heapq.heappush(frontier, (graph[current_node]['h(n)'], current_node))  
    explore.append(current_node)
    while(frontier):
        current_heuristic, current_node = heapq.heappop(frontier)
       
        if current_node==goal_node:
            print("Goal reached")
            return explore
        if current_node not in explore:
            explore.append(current_node)  
            expand.append(current_node)
            
    
        for child in graph[current_node]['Child']:
            print(f"child:{child}")
            if child not in  explore:
                heapq.heappush(frontier, (graph[child]['h(n)'], child))  


    print("Goal not found")
    return explore


print(Best_FS(graph, '1','5'))



