"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # this will hold edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)   # there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex)

        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)                

                # Do something with the node
                print(v)

                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)            
        

    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push(starting_vertex_id)

        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)               

                # Do something with the node
                print(v)                

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)
   

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            # print(f"visited {starting_vertex}")
            for next_vert in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vert, visited)
        

    def bfs(self, starting_vertex_id, target_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex_id])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                if v == target_vertex_id:
                      return path

                # Mark it as visited...
                visited.add(v)

                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK

                for next_vert in self.get_neighbors(v):
                    new_path = list(path)  # Copy the list
                    new_path.append(next_vert)
                    q.enqueue(new_path)

        # If we got here, we didn't find it
        return None
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        vert_stack = Stack()

        visited = set()

        vert_stack.push(starting_vertex)
        vert_path = []

        while vert_stack.size() > 0:
            vert_path.append(vert_stack.pop())

            last_vert = vert_path[-1]
            if last_vert not in visited:
                if last_vert == destination_vertex:
                    return vert_path
                visited.add(last_vert)
                # print(f"visited {v}")
                for next_vert in self.get_neighbors(last_vert):
                    vert_stack.push(next_vert)
        return visited
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
            path.append(starting_vertex)

        # visited.add(starting_vertex)

        if starting_vertex not in visited:
            # print(path)
            visited.add(starting_vertex)
            if path[-1] == destination_vertex:
                return path
            # print(f"visited {starting_vertex}")
            for next_vert in self.get_neighbors(starting_vertex):
                copy_path = list(path)
                copy_path.append(next_vert)
                next_path = self.dfs_recursive(next_vert, destination_vertex, visited, copy_path)
                # print(next_path)
                if next_path is not None:
                    return next_path
        else:
            return


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
