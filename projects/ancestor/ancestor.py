# from graph import Graph

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

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # Create an empty stack
    s = Stack()    
    # Create a set to store the visited nodes
    visited = set()
    # Init: push the starting node
    s.push(starting_node)    
    # current parents
    parents = set()

    # While the stack isn't empty
    while s.size() > 0:
        # pop the first item
        v = s.pop()
        # If it's not been visited:
        if v not in visited:
            # Mark as visited (i.e. add to the visited set)
            visited.add(v)
            
            for g in get_parents(v, ancestors):
                if g:
                    parents = set()                   
                    parents.add(g)
                    s.push(g)

    if len(parents) > 0:
        return min(parents)
    else:
        return -1

        # graph = Graph()
        # for pair in ancestors:
        #     if pair[0] not in graph.vertices:
        #         graph.add_vertex(pair[0])
        #     if pair[1] not in graph.vertices:
        #         graph.add_vertex(pair[1])
        #     graph.add_edge(pair[1], pair[0])
        # q = Queue()
        # longest_path = []
        # # node_location = 0
        # q.enqueue(starting_node)
        # while q.size() > 0:
        #     deq = q.dequeue()
        #     if len(deq) > len(longest_path):
        #         longest_path = deq
        #     if len(deq) == len(longest_path):
        #         if deq[-1] < longest_path[-1]:
        #             longest_path = deq
        #     for neighbor in graph.get_neighbors(deq[-1]):
        #         temp_path = deq.copy()
        #         temp_path.append(neighbor)
        #         q.enqueue(temp_path)
        # if len(longest_path) <= 1:
        #     return -1
        # return longest_path[-1]

def get_parents(child, parent):    
    parents = set()
    for ancestor in parent:        
        p = ancestor[0]        
        ch = ancestor[1]
        if ch == child:            
            parents.add(p)
    return parents