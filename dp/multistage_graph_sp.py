
def find_shortest_distance(graph):
    pass



if __name__ == "__main__":
    # Driver code  
    N = 8
    INF = 999999999999
    
    # Graph stored in the form of an  
    # adjacency Matrix  
    graph = [
        [INF, 1, 2, 5, INF, INF, INF, INF],  
        [INF, INF, INF, INF, 4, 11, INF, INF],  
        [INF, INF, INF, INF, 9, 5, 16, INF],  
        [INF, INF, INF, INF, INF, INF, 2, INF],  
        [INF, INF, INF, INF, INF, INF, INF, 18], 
        [INF, INF, INF, INF, INF, INF, INF, 13],  
        [INF, INF, INF, INF, INF, INF, INF, 2]
    ]  
    
    print(find_shortest_distance(graph)) 