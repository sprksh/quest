"""
Presenting a comprehensive explanation of Graph traversal, BFS & DFS
dag: Directed Acyclic Graph

"""


class Graph:
    """
    This is a directed graph.
    What happens in a non directed graph?
    """

    def __init__(self, graph):
        self.graph = graph      # defaultdict(list)

    def breadth_first_search(self, root):
        """
        In BFS, we first cover all neighbours and add all seen neighbours to queue
        then we keep visiting whatever is there in queue and removing that from queue

        Note: there is a difference between seeing and visiting
        when you find a neighbour and add it to q for visiting later, it is seen but not visited
        when you visit a node, you add its neighbours to queue
        """
        print("performing a breadth first search")
        seen, visited, queue = set(), [], [root]
        # can use collections.deque instead of normal list
        # seen is a set because we need to look up if the new element is there in seen or not: O(1)
        while queue:
            print("Present queue: %s" % str(queue))
            vertex = queue.pop(0)
            print("Finding neighbours of: %s" % vertex)
            visited.append(vertex)
            if self.graph[vertex]:
                for neighbour in self.graph[vertex]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        queue.append(neighbour)
                        print("added %s to queue" % neighbour)
                    else:
                        print("Neighbour %s is already visited" % neighbour)
            else:
                print("No neighbours for %s" % vertex)
        print("Seen nodes: %s" % str(seen))
        print("Visited nodes in order: %s" % str(visited))

    def depth_first_search(self, root):
        """
        Basically there is no difference in seeing and visiting.
        You see it, you visit it. recursively here
        """
        print("performing a depth first search")
        visited = set()
        explored = []
        found = []

        def dfs(graph, node):
            found.append(node)
            if node not in visited:
                visited.add(node)
                print("Exploring node: %s" % node)
                if graph[node]:
                    for n in graph[node]:
                        print("Found %s as neighbour of %s" % (n, node))
                        dfs(graph, n)
                else:
                    print("No neighbour found for %s, returning back" % node)
                explored.append(node)
            else:
                print("Node %s already explored" % node)

        dfs(self.graph, root)

        print("Visited nodes: %s" % str(visited))
        print("Exploration of nodes completed in order: %s" % str(explored))
        print("Found nodes in order: %s" % str(found))

    def iterative_dfs(self, root):
        """
        https://stackoverflow.com/a/9201268/4510252
        basically instead of queue, we use stack
        only difference between stack and queue is in a stack, we get elements from end and in queue, we get from start
        # pop(0) for queue
        # pop() for stack
        """
        print("performing an iterative depth first search")
        seen, visited, stack = set(), [], [root]
        while stack:
            print("Present stack: %s" % str(stack))
            vertex = stack.pop()
            print("Finding neighbours of: %s" % vertex)
            visited.append(vertex)
            if self.graph[vertex]:
                for neighbour in self.graph[vertex]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
                        print("added %s to stack" % neighbour)
                    else:
                        print("Neighbour %s is already visited" % neighbour)
            else:
                print("No neighbours for %s" % vertex)
        print("Seen nodes: %s" % str(seen))
        print("Visited nodes: %s" % str(visited))

    def recursive_bfs(self):
        """
        # is there a recursive bfs? not directly, not useful.
        https://stackoverflow.com/questions/2549541/performing-breadth-first-search-recursively
        # but its about bfs on binary tree
        """
        pass

    def dfs_with_cyclic(self):
        pass

    def bfs_with_cyclic(self):
        pass


if __name__ == '__main__':
    # graph repr as adjacency list
    """
    graph image link for better understanding from educative
    https://www.educative.io/api/edpresso/shot/4915476100546560/image/5205102925185024
    """
    graph = {
              'A': ['B', 'C'],
              'B': ['D', 'E'],
              'C': ['F'],
              'D': [],
              'E': ['F'],
              'F': []
            }
    g = Graph(graph)
    g.breadth_first_search("A")
    print("\n")
    g.depth_first_search("A")
    print("\n")
    g.iterative_dfs("A")
