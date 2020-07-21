class Solution:
    def allPathsSourceTarget(self, graph):
        root = 0
        destination = len(graph) -1
        all_paths = []
        
        def traverse_dfs(node, path):
            if node == destination:
                print(path)
                all_paths.append(path.copy())
                return True

            for adjacent_node in graph[node]:
                print(path)
                print(adjacent_node)
                path.append(adjacent_node)
                traverse_dfs(adjacent_node, path)
                path.pop()
        
        traverse_dfs(root, path=[0])
        return all_paths
                
                    
if __name__ == "__main__":
    Solution().allPathsSourceTarget([[1,2], [3], [3], []])
