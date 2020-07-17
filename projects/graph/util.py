
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# class Graph:
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set()
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             print('Vertex not found')
# new_graph = Graph()
# new_graph.add_vertex(1)
# new_graph.add_vertex(2)
# new_graph.add_edge(1, 2)
# #### WITHOUT GRAPH CLASS ####            
# whatever = {}
# whatever[1] = set()
# whatever[2] = set()
# whatever[1].add(2)

